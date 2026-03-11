"""
Entry point of the application.

Creates the FastAPI application instance, registers API routes,
initializes the database connection, and starts the API service.
"""

from fastapi import FastAPI
from routes import items
from database import engine, Base
from logger import setup_logger
import logging

setup_logger()

logger = logging.getLogger(__name__)

logger.info('Application starting up')

#Create an instance of FastAPI
app = FastAPI()

logger.info('Starting up the router')
app.include_router(items.router)

#Create tables in database if they don't already exist
Base.metadata.create_all(bind = engine)

#Health check to ensure the application is up and running
@app.get("/")
def root():
    return {"message": "Reading List API is running"}
