#Defines response and request data formats

from pydantic import BaseModel
from datetime import datetime
from typing import Generic, List, TypeVar

T = TypeVar('T')
class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool

#Schema for creating an item
class ItemCreate(BaseModel):
    title: str
    author: str
    notes: str | None = None
    read: bool

#Schema for updating an item
class ItemUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    notes: str | None = None
    read: bool | None = None

#Schema for returning an item
class ItemResponse(BaseModel):
    class Config:
        orm_mode = True
    id: int
    title: str
    author: str
    notes: str | None = None
    read: bool
    created_at: datetime

