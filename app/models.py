#Defines the structure of the database

from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from datetime import datetime
from database import Base

#Represents the database table
class ReadingItem(Base):
    __tablename__ = "reading_items"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False)
    author = Column(String, nullable = False)
    notes = Column(Text, nullable = True)
    read = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.utcnow)
    
    #Represents how the objects prints in the console
    def __repr__(self):
            return f"<ReadingItem(title='{self.title}', author='{self.author}', read={self.read})>"