FROM python:3.7.3-stretch

WORKDIR /app

ADD . /app

RUN apt update

RUN apt install ffmpeg -y

RUN pip install -r requirements.txt

CMD ["uwsgi", "ytopod.ini"]