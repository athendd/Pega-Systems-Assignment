# Pega-Systems-Assignment

A small service for managing a reading list of books. Every book has:
  - title
  - author
  - notes
  - read/unread status (labeled as read)
  
Users can create, retrieve, update, and delete items from their reading list. 

## Folder Strucutre

Pega-Systems-Assignment
├──README.md
├──app
│  ├──main.py
│  └──schemas.py
│  └──models.py
│  └──database.py
│  └──logger.py
│  └──config.py
│  └──Dockerfile
│  └──.env
│  └──app.log
│  └──reading_list.db
│  └──requirements-pro.txt
│  └──requirements.txt
│  └──routes/
│     └──items.py
│  └──services
│     └──item_service.py


## AI's Impact

  - Recommended SQLite as database engine for project.
  - Recommended using Pydantic models to ensure proper formatting in responses and requests.
  - Recommended using SQLAlchemy to enable interactions between database and application.
  - Recommended using a config file to keep track of environment variables.
  - Taught me to use `Union` types to accept different return types, allowing the GET all items endpoint to work with or without pagination.
  - Recommended using logging to track data flow and potential issues.
  - Recommended writing tests to verify the application's functionality.
  - Taught me about `StaticPool`, which allows tests to run using a single shared in-memory connection, enabling testing while the application is running. 

## Tools and their Purpose

### Docker
Used to containerize the application, allowing it to run consistently across different operating systems or environments. 

### FastAPI
A high-performance web framework ideal for building small services such as this application. Uses asynchronous programming for speed and integrates seamlessly with Pydantic models for request/response validation. 

### Uvicorn
A fast, lightweight ASGI server for running FastAPI applications. Chosen for its compatibility with FastAPI and asynchronous support.

### SQLite
A lightweight, serverless relational database stored in a single file. Requires no setup, making it ideal for small projects. An in-memory version is used during testing to prevent modifying the main database. 

### Pydantic Models
Define the data structure of requests and responses. They validate input and output data automatically, reducing errors and simplifying API development.

### SQLAlchemy
An Object-Relational Mapper (ORM) that maps Python classes to database tables. Enables easy interaction between Python objects and the database, including automatic table creation, querying, and updates.

## Setup Application

1. Download or clone the repository.

2. Open up the repository on an IDE (like Visual Studio Code)

3. Navigate to the app directory:
  ```bash
  cd app
   ```
4. Install the dependencies:
  ```bash
  cd app
  ```

5. Start the server:
    ```bash
    python -m uvicorn main:app --reload
    ```

6. Copy the link given in the terminal:
    http://127.0.0.1:8000
   
7. Open your browser and enter the link with `/docs` at the end:
    http://127.0.0.1:8000/docs

### 8. **Using API Routes**

```markdown
## Using the API Routes

All API routes are accessible via the Swagger documentation at `/docs` once the server is running. Here's how to interact with them:

1. Click down arrow to expand a route and press `Try it out`.

2. Enter required parameters:
  - **Get Item**: Enter `item_id`
   - **Update Item**: Enter `item_id` and the new values in the request body.
   - **Delete Item**: Enter `item_id`.
   - **Create Item**: Enter title, author, read status, and optional notes.
   - **Get All Items**: Optional `page` and `page_size` parameters for pagination.

3. Press **Execute** to see the response.

You can also use cURL or Postman to make requests to these endpoints.

```

## Instructions for Docker

1. Create a Docker Image with the dockerfile:

2. Open up Docker Desktop:
  
3. Click on run button:

4. Enter the environment variables (in project folder's .env file):

5. Click on run:

6. Test the application:
   

## Instructions for Testing

*Server does not need to be running in order to run tests

1. Open a new terminal and navigate to the app directory.

2. Run tests with pytest:
   ```bash
   python -m pytest
   ```

## Instructions for Each Route

### Get An Item

1. Go down to Get Item route and press on down arrow:

2. Press the Try it out button:

3. Enter in ID (integer) in item_id box

4. Press the Execute button

5. Scroll down to see the results

### Update An Item

1. Go down to Update Item route and press on down arrow:

2. Press the Try it out button:

3. Enter in ID (integer) in item_id box

4. Then scroll down to Request body and enter the new values

4. Then press the Execute button

5. Scroll down to see the results

### Delete An Item

1. Go down to Delete Item route and press on down arrow to the left of it

2. Press the Try it out button

3. Then enter in ID (integer) in item_id box

4. Then press the Execute button

5. Scroll down to see the results

### Create An Item

1. Go down to Create Item route and press on down arrow to the left of it

2. Press the Try it out button

3. Then under Request body, enter values for new item

4. Then press the Execute button

5. Scroll down to see the results

### Get All Items

1. Go down to Get All Items route and press on down arrow to the left of it

2. Press the Try it out button

3. Optional: Enter an integer in page box and an integer in page_size box if you want to use pagination

4. Then press the Execute button

5. Scroll down to see the results

## Instructions to Containzerize Application

1. Run the Dockerfile to generate a Docker Image:

2. Open up Docker Desktop, and press the Run button for the image

3. Enter the key and value pairs for environment variables and set the port

4. Open link on web browser and see the results
