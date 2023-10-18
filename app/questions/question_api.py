from datetime import datetime
from fastapi import HTTPException, status
import httpx

from app.questions.dao import QuestionsDAO

async def fetch_data(num: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://jservice.io/api/random?count={num}')
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="invalid request"
            )


async def add_questions(num: int):
    data = await fetch_data(num)
    
    for q in data:
        while await QuestionsDAO.find_by_id(q['id']):
            q = await fetch_data(1)[0]
        await QuestionsDAO.add_question(question_id=q['id'], answer=q['answer'], question=q['question'], created_at=datetime.strptime(q['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'))
