from pydantic import BaseModel, validator


class QuestionNum(BaseModel):
    question_num: int

    class Config:
        orm_mode = True

    @validator('question_num')
    def num_validate(cls, question_num):
        if question_num > 0:
            return question_num
        raise ValueError('Invalid question num')


class Question(BaseModel):
    question_id: int
    question: str
    answer: str
    created_at: str

    class Config:
        orm_mode = True
