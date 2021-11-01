FROM python:slim

RUN useradd converter

WORKDIR /home/converter

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app

COPY converter.py boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP converter.py

RUN chown -R converter:converter ./

USER converter
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]