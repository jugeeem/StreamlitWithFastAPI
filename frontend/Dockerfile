FROM node:22-alpine3.19

RUN apk update && apk add curl

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .
