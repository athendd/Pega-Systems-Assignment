from models import ReadingItem
from schemas import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException


def get_all_items_service(db: Session):
    return db.query(ReadingItem).all()

def get_item_service(db: Session, item_id: int):
    item = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code = 404, detail = 'Item not found')
    
    return item

def create_item_service(db: Session, item: ItemCreate):
    new_item = ReadingItem(
        title = item.title, 
        author = item.author,
        notes = item.notes
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

def delete_item_service(db: Session, item_id: int):
    item_to_delete = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item_to_delete:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item_to_delete)
    db.commit()

def update_item_service(db: Session, item_id: int, updated_item: ItemUpdate):
    item_to_update = db.query(ReadingItem).filter(ReadingItem.id == item_id).first()
    if not item_to_update:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = updated_item.model_dump(exclude_unset = True)
    for key, value in update_data.items():
        setattr(item_to_update, key, value)

    db.commit()
    db.refresh(item_to_update)

    return item_to_update
    
