FROM python:3.10.5-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/app
WORKDIR /var/app
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN apk del .build-deps

EXPOSE 5000