
ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


ENV DB_NAME=inventory
ENV NODE_ID=6
ENV NODE_NAME=InventoryManager
ENV RABBITMQ_QUEUE_HEALTH=health
ENV RABBITMQ_QUEUE_PRODUCT=product
ENV INTERVAL=10
ENV PROFIT_MARGIN=0.2


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


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY . .

EXPOSE 8501

CMD streamlit run streamlit.py
