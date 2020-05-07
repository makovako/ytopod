FROM python:3.7.3-stretch

WORKDIR /app

ADD . /app

RUN apt update

RUN apt install ffmpeg -y

RUN pip install -r requirements.txt

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
    
RUN chown -R appuser:appuser /app

USER appuser


CMD ["uwsgi", "ytopod.ini"]