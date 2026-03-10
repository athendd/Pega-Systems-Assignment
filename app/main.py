"""
Entry point of the applicaiton where FastAPI applicaiton instance is created,
API routes are registered, intializes connection to database, and starts
API service
"""

from fastapi import FastAPI
from routes import items
from database import engine, Base

#Create an instance of FastAPI
app = FastAPI()
app.include_router(items.router)

#Create tables in database if they don't already exist
Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "Reading List API is running"}
