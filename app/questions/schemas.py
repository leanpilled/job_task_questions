from pydantic import BaseModel

class QuestionSchema(BaseModel):
    question: str
    answer: str

class QuestionRequest(BaseModel):
    questions_num: int
