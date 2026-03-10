"""
Configure and manage the database connection.

Initializes the SQLAlchemy engine and session factory used
throughout the application.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from config import Settings

settings = Settings()
database_url = settings.database_url

engine = create_engine(database_url, echo = True)

session = sessionmaker(autocommit = False, bind = engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()