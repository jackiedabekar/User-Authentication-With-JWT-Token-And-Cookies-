FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install -r requirements.txt

COPY . /app/