from typing import Optional
from sqlalchemy import insert, select
from app.db import async_session_maker
from app.questions.models import Questions
from app.questions.schemas import QuestionSchema

class QuestionsDAO:
            
    @classmethod
    async def add_question(cls, **data):
        async with async_session_maker() as session:
            query = insert(Questions).values(**data)
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def find_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(Questions).filter_by(question_id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def get_latest_question(cls) -> Optional[QuestionSchema]:
        async with async_session_maker() as session:
            query = select(Questions).order_by((Questions.id.desc())).limit(1)
            question = (await session.execute(query)).scalar_one_or_none()
            if question is None:
                return None
            return QuestionSchema(question=question.question, answer=question.answer)
