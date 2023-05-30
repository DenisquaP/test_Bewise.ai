import requests


def get_questions(question_num: int = 1) -> list:
    return requests.get(f'https://jservice.io/api/random?count={question_num}').json()  # noqa 501
