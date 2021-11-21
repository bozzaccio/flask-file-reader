FROM python:3.8-slim

RUN useradd converter

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv venv

RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY . /app

RUN chmod 777 -R uploads
RUN chmod +x boot.sh

ENV FLASK_APP app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]