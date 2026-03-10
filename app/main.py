"""
Entry point of the application.

Creates the FastAPI application instance, registers API routes,
initializes the database connection, and starts the API service.
"""

from fastapi import FastAPI
from routes import items
from database import engine, Base
from config import Settings

settings = Settings()

#Create an instance of FastAPI
app = FastAPI()
app.include_router(items.router)

#Create tables in database if they don't already exist
Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "Reading List API is running"}
