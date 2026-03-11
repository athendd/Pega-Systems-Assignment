"""
Service layer for reading list items.

Contains the business logic for CRUD operations and pagination.
Separates database logic from API routes.
"""

from models import ReadingItem
from schemas import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import PaginatedResponse
import math
import logging


logger = logging.getLogger(__name__)

def get_all_items_service(db: Session, page: int = None, page_size: int = None):
    """
    Retrieves reading items from the database.

    If page and page_size are given, results are paginated. 
    Else all items are returned.

    Args:
        db (Session): Database session.
        page (int | None): Page number for pagination.
        page_size (int | None): Number of items per page.

    Returns:
        List[ReadingItem] | PaginatedResponse[ReadingItem]
    """
    if page is None or page_size is None:
        logger.info('Did not use pagination for retrieval')
        return db.query(ReadingItem).all()

    logger.debug(f'Fetching items page: {page}, page_size: {page_size}')

    #Calculate how many records to skip for pagination
    offset = (page - 1) * page_size
    logger.debug(f'Calculated offset: {offset}')
    total = db.query(ReadingItem).count()
    items = (
        db.query(ReadingItem)
        .order_by(ReadingItem.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    total_pages = math.ceil(total/page_size)
    logger.debug(f'Total Pages: {total_pages}')


    return PaginatedResponse(items = items, total = total, 
                             page = page, page_size = page_size,
                             total_pages = total_pages, has_next = page < total_pages,
                             has_prev = page > 1)


def get_item_service(db: Session, item_id: int):
    """
    Retrieve a single reading item by ID.

    Raises:
        HTTPException: If the item does not exists.

    Args:
        db (Session): Database session.
        item_id (int): ID of item to retrieve.

    Returns:
        ReadingItem
    """
    item = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item:
        logger.warning(f'Item with id {item_id} not found')
        raise HTTPException(status_code = 404, detail = 'Item not found')
    
    return item

def create_item_service(db: Session, item: ItemCreate):
    """
    Create a new reading item in the database.

    Validates required fields before inserting the record.

    Args:
        db (Session): Database session.
        item (ItemCreate): Item to be added to database.

    Returns:
        ItemCreate
    """
    logger.info(f'Creating reading item with title: {item.title} and author: {item.author}')
    new_item = ReadingItem(
        title = item.title, 
        author = item.author,
        notes = item.notes,
        read = item.read
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    logger.info(f'Created item with id: {new_item.id}')

    return new_item

def delete_item_service(db: Session, item_id: int):
    """
    Delete a single reading item by ID.

    Raises:
        HTTPException: If item does not exist in database.

    Args:
        db (Session): Database session.
        item_id (int): ID of item to delete.
    """
    item_to_delete = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    logger.info(f'Deleting item with id: {item_id}')
    if not item_to_delete:
        logger.warning(f'Attempted to delete non-existent item with id: {item_id}')
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item_to_delete)
    db.commit()

def update_item_service(db: Session, item_id: int, updated_item: ItemUpdate):
    """
    Update fields of an existing reading item.

    Raises:
        HTTPException: If item does not exist in database.

    Args:
        db (Session): Database session.
        item_id (int): ID of item to be updated.
        updated_item (ItemUpdate): Updated item.

    Returns:
        ItemUpdate
    """

    item_to_update = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item_to_update:
        logger.warning(f'Item with id {item_id} not found')
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = updated_item.model_dump(exclude_unset = True)
    logger.debug(f"Updated fields: {list(update_data.keys())}")
    for key, value in update_data.items():
        if (key == 'title' and not value) or (key == 'author' and not value):
            continue

        setattr(item_to_update, key, value)

    db.commit()
    db.refresh(item_to_update)

    return item_to_update