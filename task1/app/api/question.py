from fastapi import Depends, APIRouter
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from functions.create_entry import create_new_entry
from functions.get_question_from_api import get_questions
from tables import Questions
from database import get_session
from schemas.question import QuestionNum, Question


question_router = APIRouter()


@question_router.post(
        '/question/',
        status_code=201,
        response_model=List[Question],
        tags=['Question']
        )
async def question(question: QuestionNum, db: AsyncSession = Depends(get_session)):  # noqa 501
    result = await db.execute(Select(Questions.question_id))
    questions_in_bd = result.scalars().all()

    question_num = question.dict().get('question_num')
    questions = []
    response = await get_questions(question_num)
    for i in response:
        if i.get('id') in questions_in_bd:
            new_question = await get_questions()[0]
            while new_question.get('id') in questions_in_bd:
                new_question = await get_questions()[0]
            questions.append(create_new_entry(new_question))
            db.add(create_new_entry(new_question))
            continue

        questions.append(create_new_entry(i))
        db.add(create_new_entry(i))
    await db.commit()
    return questions
