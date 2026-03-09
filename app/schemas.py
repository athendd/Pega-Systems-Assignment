#Defines response and request data formats

from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
    title: str
    author: str
    notes: str | None = None

class ItemUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    notes: str | None = None
    read: bool | None = None

class ItemResponse(BaseModel):
    class Config:
        orm_mode = True
    id: int
    title: str
    author: str
    notes: str | None = None
    read: bool
    created_at: datetime

