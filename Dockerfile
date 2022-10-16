FROM python:3.8-slim-buster


COPY .. /app
COPY requeriments.txt ../app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requeriments.txt


COPY . .
RUN export FLASK_APP=routes.py 