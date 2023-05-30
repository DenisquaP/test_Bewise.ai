FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY app/alembic.ini code/alembic.ini

ENV ALEMBIC_CONFIG=code/alembic.ini
