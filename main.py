"""
Module for FastAPI creation
"""
from loguru import logger
import uvicorn
from fastapi import FastAPI
from schemas.fastapi_schemas import User, Quiz, CareerPathRequest
from database.mongodb import MongoDB
from endpoint_modules.generate_quiz import generate_quiz_from
from endpoint_modules.generate_career_path import generate_career_path
from fastapi.middleware.cors import CORSMiddleware
import json


app = FastAPI(title="genius_guru_backend")

origins = [ "*" ] #TODO: update this to limit requests for sepecific origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoDB()

@app.post("/generate_career_path")
async def generate_career_path_api(submitted_quiz: Quiz):
    """
    Post end-point for submitting the quiz
    """

    with open("offline_database/courses/Courses.json", "r") as json_file:
        courses = json.load(json_file)

    return generate_career_path(submitted_quiz, courses)


@app.post("/sign_up")
async def sign_up(user_data: User):
    """
    Post end-point for user sign up
    """
    client.add_user(user_data)


@app.get("/get_quiz", response_model=Quiz)
async def get_quiz(user_major):
    """
    Get end-point for quiz generation
    """

    quiz = generate_quiz_from(user_major)

    return quiz


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
