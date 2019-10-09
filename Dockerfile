FROM python:3.7-alpine
MAINTAINER Egor Kostan

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk update && \
    apk upgrade && \
    apk add git && \
    apk add mercurial

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
