from fastapi import FastAPI
from routes import items
from database import engine, Base

#Create an instance of FastAPI
app = FastAPI()
app.include_router(items.router)

#Create tables in database if they don't exist
Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "Reading List API is running"}
