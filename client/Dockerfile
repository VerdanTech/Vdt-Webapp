FROM node:latest

WORKDIR /client_workdir

COPY package*.json .

RUN npm install

COPY ./verdantech_client .

CMD ["npm", "run", "dev"]
