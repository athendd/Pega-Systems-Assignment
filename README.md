# Pega-Systems-Assignment

A small service for managing a reading list of books. Every book has:
  - title
  - author
  - notes
  - read/unread status (labeled as read)
  
Users can create, retrieve, update, and delete items from their reading list. 

## AI's Impact

  - Recommended SQLite as database engine for project.
  - Recommended using Pydantic models to ensure proper formatting in responses and requests.
  - Recommended using SQLAlchemy to enable interactions between database and application.
  - Recommended using a config file to keep track of environment variables.
  - Taught me to use unions as a way to accept different return types which allowed get all items to work with and without pagination.
  - Recommended using logger to keep track of data flow and issues.
  - Recommended I use tests to test the application's functionalities.
  - Taught me about StaticPool which allowed testing to run at the same time as the application with their being just one shared connection. 

## Tools and their Purpose

### Docker
Can be used to containerize the application on run on other operating systems or devices. 

### FastAPI
Ideal for a small service such as this because it uses asynchronous programming to achieve high performance since it's built on an ASGI server. It also integrates with Pydantic models which I'll explain the benefits of down below.

### Uvicorn
Fast, lightweight ASGI for Python that runs asynchronous web applications frameworks such as FastAPI. Mostly chosen due to its compatability with FastAPI. 

### SQLite
Light, serverless relational database engine that stores a database in a single file. Requires no setup and servers making it easy to use for a small service. 

### Pydantic Models
Models that define data structure which help to ensure proper formatting and procedures for responses and requests. 

### SQLAlchemy
ORM (Object-Relational Mapper) that allows python objects to represent tables in database. Allowed easy interaction between applicaiton and database since objects could be converted to tables and vice versa. 

## Instructions to Start Application

1. Download the project folder to your local device.

2. Open up the project folder on an IDE (like Visual Studio Code)

3. Navigate to the app directory:
  ```bash
  cd app
   ```
4. Install the dependencies:
  ```bash
  cd app```

5. Start the server:
    ```bash
python -m uvicorn main:app --reload
```

6. Copy the link given in the terminal:
   
7. Enter it into a web browser with /docs at the end:


## Instructions for Docker

1. Create a Docker Image with the dockerfile:

2. Open up Docker Desktop:
  
3. Click on run button:

4. Enter the environment variables (in project folder's .env file):

5. Click on run:

6. Test the application:
   

## Intructions to Run Tests

*Server does not need to be running in order to run tests

1. Open a new terminal and navigate to the app directory.

2. Run tests with pytest:
   ```bash
   python -m pytest
   ```

## Instructions for Each Route

### Get An Item

1. Go down to Get Item route and press on down arrow to the left of it

2. Press the Try it out button

3. Then enter in ID (integer) in item_id box

4. Then press the Execute button

5. Scroll down to see the results

### Update An Item

1. Go down to Update Item route and press on down arrow to the left of it

2. Press the Try it out button

3. Then enter in ID (integer) in item_id box

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

3. Optional: Enter an integer in page box and an integer in page_size box if oyu want to use pagination

4. Then press the Execute button

5. Scroll down to see the results

## Instructions to Containzerize Application

1. Generate an image from the Dockerfile

2. Open up Docker Desktop, and press the Run button for the image

3. Entire the key and value pairs for enironment variables and set the port

4. Open link on web browser and see the results
