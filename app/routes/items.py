#Defines the API routes related to items
from services.item_service import get_item_service, update_item_service, delete_item_service, create_item_service, get_all_items_service, get_all_items_with_pagination_service
from fastapi import APIRouter, Depends, Query
from database import get_db
from schemas import ItemResponse, ItemUpdate, ItemCreate, PaginatedResponse
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix = '/items')

@router.get('/{item_id}', response_model = ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return get_item_service(db, item_id)

@router.put('/{item_id}', response_model = ItemResponse)
def update_item(item_id: int, updated_item: ItemUpdate, db: Session = Depends(get_db)):
    return update_item_service(db, item_id, updated_item)

@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    delete_item_service(db, item_id)

@router.post('/', response_model = ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item_service(db, item)

@router.get('/', response_model = List[ItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    return get_all_items_service(db)

@router.get('_with_pagination/',  response_model = PaginatedResponse[ItemResponse])
def get_all_items(page: int = Query(1, ge = 1), page_size: int = Query(20, ge = 1, le = 100, description = 'Items per page'), db: Session = Depends(get_db)):
    return get_all_items_with_pagination_service(page, page_size, db)