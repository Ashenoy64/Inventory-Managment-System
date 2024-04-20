ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_PASS=shenoy@72
ENV DB_USER=postgres
ENV DB_NAME=inventory
ENV NODE_ID=3
ENV NODE_NAME=CreateAndUpdate
ENV INTERVAL=10
ENV RABBITMQ_QUEUE_HEALTH=health
ENV RABBITMQ_QUEUE_PRODUCT=product
ENV RABBITMQ_HOST=localhost
ENV RABBITMQ_PORT=5672

CMD python create_update.py
