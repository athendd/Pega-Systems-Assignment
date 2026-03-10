from models import ReadingItem
from schemas import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import PaginatedResponse
import math

"""
Retrieves reading items from the database.

If page and page_size are given, results are paginated. 
Else all items are returned

Args:
"""
def get_all_items_service(db: Session, page: int = None, page_size: int = None):
    if page is None or page_size is None:
        return db.query(ReadingItem).all()

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

#Retrieves a single item from the database based on the given id
def get_item_service(db: Session, item_id: int):
    item = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code = 404, detail = 'Item not found')
    
    return item

#Creates an item in the database
def create_item_service(db: Session, item: ItemCreate):
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

#Deletes an item from the database
def delete_item_service(db: Session, item_id: int):
    item_to_delete = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item_to_delete:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item_to_delete)
    db.commit()

#Updates an item in the database
def update_item_service(db: Session, item_id: int, updated_item: ItemUpdate):
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
    
