"""
Configure and manage the database connection.

Initializes the SQLAlchemy engine and session factory used
throughout the application.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from config import Settings
import logging

logger = logging.getLogger(__name__)

settings = Settings()

database_url = settings.database_url

logger.info('Creating the engine')
engine = create_engine(database_url, echo = True)

logger.info('Creating the session')
LocalSession = sessionmaker(autocommit = False, bind = engine)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
        logger.info('Database has been obtained')
    finally:
        db.close()
        logger.info('Database session has ended')