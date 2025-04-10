from fastapi import APIRouter
from pydantic import BaseModel
from services.quiz_service import grade_answer

router = APIRouter()

class SubmitRequest(BaseModel):
    question: str
    choices: list[str]  # 4개 보기
    user_answer: str    # 예: "C"

@router.post("/submit-answer")
def submit_answer(data: SubmitRequest):
    result = grade_answer(data.question, data.choices, data.user_answer)
    return result
