ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


ENV DB_NAME=inventory
ENV NODE_ID=3
ENV NODE_NAME=CreateAndUpdate
ENV INTERVAL=10
ENV RABBITMQ_QUEUE_HEALTH=health
ENV RABBITMQ_QUEUE_PRODUCT=product

WORKDIR /app
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Installing the application in editable mode
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

USER appuser

COPY . .



CMD python create_update.py

