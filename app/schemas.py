"""
Schemas that define request and response data format 
using Pydantic models
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Generic, List, TypeVar

T = TypeVar('T')
class PaginatedResponse(BaseModel, Generic[T]):
    """
    Generic schema used for paginated API response
    """
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool

class ItemCreate(BaseModel):
    """
    Schema used for created item requests
    """
    title: str 
    author: str
    notes: str | None = None
    read: bool

class ItemUpdate(BaseModel):
    """
    Schema used for updated item requests
    """
    title: str | None = None
    author: str | None = None
    notes: str | None = None
    read: bool | None = None

class ItemResponse(BaseModel):
    """
    Schema used for API responses
    """
    class Config:
        orm_mode = True
    id: int
    title: str
    author: str
    notes: str | None = None
    read: bool
    created_at: datetime

