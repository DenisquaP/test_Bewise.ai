from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from ..functions.create_entry import create_new_entry
from ..functions.get_question_from_api import get_questions
from ..tables import Questions

from ..database import get_session
from ..schemas.question import QuestionNum, Question


question_router = APIRouter()


@question_router.post(
        '/question/',
        status_code=201,
        response_model=List[Question],
        tags=['Question']
        )
def question(question: QuestionNum, db: Session = Depends(get_session)):
    questions_in_bd = list(map(lambda i: i[0], db.query(Questions.question_id)))  # noqa 501
    print(questions_in_bd, len(questions_in_bd))
    question_num = question.dict().get('question_num')
    questions = []
    response = get_questions(question_num)
    for i in response:
        if i.get('id') in questions_in_bd:
            new_question = get_questions()[0]
            while new_question.get('id') in questions_in_bd:
                new_question = get_questions()[0]
            questions.append(create_new_entry(new_question))
            continue

        questions.append(create_new_entry(i))
    db.add_all(questions)
    db.commit()
    print(len(questions))
    return questions
