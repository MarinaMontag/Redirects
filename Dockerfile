FROM python:3.12-slim

RUN apt-get update -y
RUN apt-get install -y git

WORKDIR /code
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile --system

EXPOSE 8000
