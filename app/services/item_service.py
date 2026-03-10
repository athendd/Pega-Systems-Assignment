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
        return db.query(ReadingItem).all()

    #Calculate how many records to skip for pagination
    offset = (page - 1) * page_size
    total = db.query(ReadingItem).count()
    items = (
        db.query(ReadingItem)
        .order_by(ReadingItem.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    total_pages = math.ceil(total/page_size)

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
        raise HTTPException(status_code = 404, detail = 'Item not found')
    
    return item

def create_item_service(db: Session, item: ItemCreate):
    """
    Create a new reading item in the database.

    Validates required fields before inserting the record.

    Raises:
        HTTPException: if item does not have value for author or title.

    Args:
        db (Session): Database session.
        item (ItemCreate): Item to be added to database.

    Returns:
        ItemCreate
    """
    new_item = ReadingItem(
        title = item.title, 
        author = item.author,
        notes = item.notes,
        read = item.read
    )

    if not new_item.title:
        raise HTTPException(status_code = 400, detail = 'Need to give a value to title')
    if not new_item.author:
        raise HTTPException(status_code = 400, detail = 'Need to give a value to author')

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

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
    if not item_to_delete:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item_to_delete)
    db.commit()

def update_item_service(db: Session, item_id: int, updated_item: ItemUpdate):
    """
    Update fields of an existing reading item.

    Raises:
        HTTPException: If updated itme does not have authro or title values.

    Args:
        db (Session): Database session.
        item_id (int): ID of item to be updated.
        updated_item (ItemUpdate): Updated item.

    Returns:
        ItemUpdate
    """
    if not updated_item.title:
        raise HTTPException(status_code = 400, detail = 'Need to give a value to title')
    if not updated_item.author:
        raise HTTPException(status_code = 400, detail = 'Need to give a value to author')

    item_to_update = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item_to_update:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = updated_item.model_dump(exclude_unset = True)
    for key, value in update_data.items():
        setattr(item_to_update, key, value)

    db.commit()
    db.refresh(item_to_update)

    return item_to_update
    
