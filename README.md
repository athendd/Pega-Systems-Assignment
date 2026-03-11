# Pega-Systems-Assignment

Built a small service that manages a reading list of books. Every book in the list has an author, title, notes, and read/unread attributes. The service allows users to manage their own reading list by creating, deleting, updating, and retrieving items from the list. 

## AI's Impact

1. I used ChatGPT to help me figure out some tools I should use for the project. I had figure out what database to use, SQLite, and what web framework to use, FastAPI. ChatGPT also gave me some other recommendations for tools to use such as Pydantic models and separating the service business logic and API routes. Finally, ChatGPT recommended I use a config file to keep track of environment variables

2. I wanted to add on pagination to the project but didn't like the way it looked on FastAPI docs. I decided to try one method that uses pagination and one that doesn't, but I found this two be confusing from the user's perspective. I decided I could make one method that could get all items with or without pagination depending on the parameters that were passed. I had trouble setting this up because I needed the method to be able to return different data types depending on if pagination was used or not. ChatGPT taught me about Union object which resolved this issue. 

3. ChatGPT recommended that I use logger to keep track of data flow and issues with the code. 

## Tools and their Purpose

### FastAPI
Ideal for a small service such as this because it uses asynchronous programming to achieve high performance since it's built on an ASGI server. It also integrates with Pydantic models which I'll explain the benefits of down below.

### Uvicorn
Fast, lightweight ASGI for Python that runs asynchronous web applications frameworks such as FastAPI. Mostly chosen due to its compatability with FastAPI. 

### SQLite
Light, serverless relational database engine that stores a database in a single file. Requires no setup and servers making it easy to use for a small service. 

### Pydantic Models
Models that define ddata structure which help to ensure proper formatting and procedures for responses and requests. 

### SQLAlchemy
ORM (Object-Relational Mapper) that allows python objects to represent tables in database. Allowed easy interaction between applicaiton and database since objects could be converted to tables and vice versa. 

## Instructions to Start Application

1. Open up the application on an IDE (like Visual Studio Code)

2. Open up a terminal and go to the project's directory (PEGA-SYSTEM-ASSIGNMENT)

3. Type cd app into the terminal to reach the app directory

4. Type pip install -r requirements.txt into the terminal and run the command

5. Type uvicorn main:app --reload into the terminal and run to start the application

6. Copy the link given in the terminal and type it into a web browser (like Google) and then put /docs after it before pressing enter

