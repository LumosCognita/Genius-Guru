"""
Module for FastAPI creation
"""
from loguru import logger
import uvicorn
from fastapi import FastAPI
from schemas.fastapi_schemas import User, Quiz, Question


app = FastAPI(title="genius_guru_backend")


@app.post("/submit_quiz")
async def submit_quiz(quiz: Quiz):
    """
    Post end-point for submitting the quiz
    """
    return quiz


@app.post("/sign_up")
async def sign_up(user_data: User):
    """
    Post end-point for user sign up
    """
    logger.info(user_data)


@app.get("/get_quiz", response_model=Quiz)
async def get_quiz():
    """
    Get end-point for quiz generation
    """
    question = Question(question_body="What is the color of the sky",
                        possible_answers=["blue", "red"],
                        correct_answer_index=0
    )

    quiz = Quiz(questions=[question])
    
    return quiz


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
