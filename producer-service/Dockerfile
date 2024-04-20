ARG NODE_VERSION=18.17.0

FROM node:${NODE_VERSION}-alpine

ENV NODE_ENV production
ENV DATABASE_USER=postgres
ENV DATABASE_HOST=localhost
ENV DATABASE_NAME=inventory
ENV DATABASE_PASSWORD=shenoy@72
ENV DATABASE_PORT=5432
ENV RABBITMQ_HOST=localhost
ENV RABBITMQ_PORT=5672
ENV RABBITMQ_QUEUE_VALIDATION=validate

WORKDIR /usr/src/app

RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev

USER node

COPY . .

EXPOSE 3000

CMD npm run dev
