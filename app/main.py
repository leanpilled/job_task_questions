from fastapi import FastAPI

from app.questions.router import router as question_router

app = FastAPI()

app.include_router(question_router)
