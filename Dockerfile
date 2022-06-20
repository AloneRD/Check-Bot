FROM python:buster
WORKDIR /app/Bot

COPY CheckBot.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
CMD python CheckBot.py

