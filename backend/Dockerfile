FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    curl \
    libpq5 

COPY . /app

WORKDIR /app

RUN pip install .
