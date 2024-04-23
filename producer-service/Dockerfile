FROM node:18

ENV DATABASE_NAME=inventory
ENV RABBITMQ_QUEUE_VALIDATION=validate


WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD npm run dev


