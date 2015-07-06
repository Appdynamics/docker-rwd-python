FROM python:2.7.10
MAINTAINER Olivier Crameri

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY client/* ./
RUN pip install --no-cache-dir -r requirements.txt
