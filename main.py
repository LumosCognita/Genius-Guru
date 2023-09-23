"""
This module is used for creating a FastAPI application.
"""

# Importing necessary libraries and modules
from loguru import logger  # For logging
import uvicorn  # ASGI server
from fastapi import FastAPI  # Web framework
from schemas.fastapi_schemas import User, Quiz  # Importing User and Quiz schemas
from database.mongodb import MongoDB  # MongoDB database connection
from endpoint_modules.generate_quiz import generate_quiz_from  # Function to generate quiz
from endpoint_modules.generate_career_path import generate_career_path  # Function to generate career path
from fastapi.middleware.cors import CORSMiddleware  # Middleware for managing Cross-Origin Resource Sharing (CORS)
import json  # For handling JSON data

# Creating an instance of FastAPI with a title
app = FastAPI(title="genius_guru_backend")

# List of allowed origins for CORS. Currently allowing all origins.
origins = ["*"]  # TODO: update this to limit requests for specific origins

# Adding CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowing the origins defined above
    allow_credentials=True,  # Allowing credentials
    allow_methods=["*"],  # Allowing all HTTP methods
    allow_headers=["*"],  # Allowing all headers
)

# Creating a MongoDB client instance
client = MongoDB()

@app.post("/generate_career_path")
async def generate_career_path_api(submitted_quiz: Quiz):
    """
    This is a POST endpoint for submitting the quiz and generating a career path.
    """
    print('submitted_quiz', submitted_quiz)  # Logging the submitted quiz

    # Loading courses from the offline database
    with open("offline_database/courses/Courses.json", "r") as json_file:
        courses = json.load(json_file)

    # Returning the generated career path based on the submitted quiz and loaded courses
    return generate_career_path(submitted_quiz, courses)


@app.post("/sign_up")
async def sign_up(user_data: User):
    """
    This is a POST endpoint for user sign up.
    """
    client.add_user(user_data)  # Adding the user to the database


@app.get("/get_quiz", response_model=Quiz)
async def get_quiz(user_major):
    """
    This is a GET endpoint for generating a quiz based on the user's major.
    """
    quiz = generate_quiz_from(user_major)  # Generating quiz
    return quiz  # Returning the generated quiz


# Running the FastAPI application using uvicorn when this module is run directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
