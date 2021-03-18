FROM python:3.8-slim

WORKDIR /code

COPY Pipfile* ./
RUN pip install pipenv
RUN pipenv install --dev --system
