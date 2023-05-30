from sqlalchemy import (
    Column,
    Integer,
    String,
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer, nullable=False,
                         name='question_id', primary_key=True)
    question = Column(String, nullable=False, name='question')
    answer = Column(String, nullable=False, name='answer')
    created_at = Column(String, nullable=False, name='created at')
