from typing import Optional
from fastapi import APIRouter

from app.questions.dao import QuestionsDAO
from app.questions.question_api import add_questions
from app.questions.schemas import QuestionRequest, QuestionSchema


router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)

@router.post("")
async def post_questions(questions: QuestionRequest) -> Optional[QuestionSchema]:
    latest_question = await QuestionsDAO.get_latest_question()
    await add_questions(questions.questions_num)
    return latest_question
