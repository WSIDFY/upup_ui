# app_server/schemas/quiz.py

from pydantic import BaseModel
from typing import List

class QuizRequest(BaseModel):
    file_path: str

class QuizSubmission(BaseModel):
    quiz_id: str
    answers: List[int]