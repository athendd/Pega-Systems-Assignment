# Pega-Systems-Assignment

A small service for managing a reading list of books. Every book has:
  -title
  -author
  -notes
  -read/unread status (labeled as read)
  
Users can create, retrieve, update, and delete items from their reading list. 

## AI's Impact

1. I used ChatGPT to help me figure out some tools I should use for the project. I had figure out what database to use, SQLite, and what web framework to use, FastAPI. ChatGPT also gave me some other recommendations for tools to use such as Pydantic models and separating the service business logic and API routes. Finally, ChatGPT recommended I use a config file to keep track of environment variables

2. I wanted to add on pagination to the project but didn't like the way it looked on FastAPI docs. I decided to try one method that uses pagination and one that doesn't, but I found this two be confusing from the user's perspective. I decided I could make one method that could get all items with or without pagination depending on the parameters that were passed. I had trouble setting this up because I needed the method to be able to return different data types depending on if pagination was used or not. ChatGPT taught me about Union object which resolved this issue. 

3. ChatGPT recommended that I use logger to keep track of data flow and issues with the code. 

4. ChatGPT also recommended I had on unit tests to test the application while building. It helped me fix the issue of the unit tests not being able to run while the application was up and running by explaining that the database for the tests only lasts 1 connection and therefore I needed one shared connection to keep it alive by using StaticPool 

## Tools and their Purpose

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
