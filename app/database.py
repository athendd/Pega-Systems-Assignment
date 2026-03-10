"""
Configure and manage the database connection.

Initializes the SQLAlchemy engine and session factory used
throughout the application.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

database_url = "sqlite:///reading_list.db"

engine = create_engine(database_url, echo = True)

session = sessionmaker(autocommit = False, bind = engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()