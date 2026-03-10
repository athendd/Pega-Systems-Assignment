"""
Pydantic schemas defining request and response data formats. 
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Generic, List, TypeVar

T = TypeVar('T')
class PaginatedResponse(BaseModel, Generic[T]):
    """
    Generic schema used for paginated API response.
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
    Schema used for creating item requests.
    """
    title: str = Field(..., min_length = 1)
    author: str = Field(..., min_length = 1)
    notes: str | None = None
    read: bool

class ItemUpdate(BaseModel):
    """
    Schema used for updating item requests.
    """
    title: str = Field(None, min_length = 1)
    author: str = Field(None, min_length = 1)
    notes: str | None = None
    read: bool | None = None

class ItemResponse(BaseModel):
    """
    Schema used for API responses.
    """
    class Config:
        orm_mode = True
    id: int
    title: str
    author: str
    notes: str | None = None
    read: bool
    created_at: datetime

