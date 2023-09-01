from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    email: str
    name: str
    date_of_birth: date
    gender: str
    location: str
    major: str
    graduation_date: date
    years_of_experience: int

class Question(BaseModel):
    question_body: str
    possible_answers: list[str]
    correct_answer_index: int

class Quiz(BaseModel):
    questions: list[Question]
