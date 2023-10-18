from datetime import date
from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base


class Questions(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
