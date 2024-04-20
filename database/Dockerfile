FROM postgres:latest

ENV NODE_ID=1
ENV NODE_NAME=Database
ENV RABBITMQ_QUEUE_HEALTH=health
ENV INTERVAL=10


RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY heart_beat.py /app/heart_beat.py
COPY Schema.sql /docker-entrypoint-initdb.d/

WORKDIR /app

EXPOSE 5432

CMD ["python3", "heart_beat.py"]
