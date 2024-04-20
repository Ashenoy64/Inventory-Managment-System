ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_PASSWORD=shenoy@72
ENV DB_USER=postgres
ENV DB_NAME=inventory
ENV NODE_ID=2
ENV NODE_NAME=HealthManager
ENV RABBITMQ_QUEUE=health
ENV RABBITMQ_HOST=localhost
ENV RABBITMQ_PORT=5672
ENV INTERVAL=10


ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .


CMD python main.py
