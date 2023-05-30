from ..tables import Questions


def create_new_entry(question_dict: dict) -> Questions:
    new_question = Questions(
                question_id=question_dict.get('id'),
                question=question_dict.get('question'),
                answer=question_dict.get('answer'),
                created_at=question_dict.get('created_at')
            )
    return new_question
