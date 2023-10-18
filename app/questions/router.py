from typing import Optional
from fastapi import APIRouter

from app.questions.dao import QuestionsDAO
from app.questions.question_api import add_questions
from app.questions.schemas import QuestionSchema


router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)

@router.post("")
async def post_questions(questions: int) -> Optional[QuestionSchema]:
    latest_question = await QuestionsDAO.get_latest_question()
    await add_questions(questions)
    return latest_question
