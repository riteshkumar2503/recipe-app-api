FROM python:3.7-alpine
MAINTAINER Ritesh Kumar Ltd

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
#temp requirements below
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
#deleting the temp requirements
RUN apk del .tmp-build-deps


# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app