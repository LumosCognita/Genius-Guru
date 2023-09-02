from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class User(BaseModel):
    username: str
    email: str
    name: str
    date_of_birth: str
    gender: str
    location: str
    major: str
    graduation_date: str
    years_of_experience: int

    def to_dict(self):
        class_dict = {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "location": self.location,
            "major": self.major,
            "graduation_date": self.graduation_date,
            "years_of_experience": self.years_of_experience
        }
        return class_dict


class Answer(BaseModel):
    id:  int
    label: str

class Question(BaseModel):
    question: str
    options: List[Answer]
    answer: int
    user_answer: Optional[int] = None

class Quiz(BaseModel):
    questions: List[Question]

class CareerPathRequest(BaseModel):
    username: str
    submitted_quiz: Quiz