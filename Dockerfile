FROM ubuntu:latest

RUN useradd converter

WORKDIR /app

COPY flask/requirements.txt requirements.txt

RUN apt-get update -y

RUN apt-get install -y pip python-dev

RUN pip3 install -r requirements.txt

COPY flask /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]