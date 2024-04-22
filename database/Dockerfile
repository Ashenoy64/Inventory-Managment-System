FROM postgres:latest

ENV NODE_ID=1
ENV NODE_NAME=Database
ENV RABBITMQ_QUEUE_HEALTH=health
ENV INTERVAL=10

#installing python and pip
RUN apt-get update && apt install -y python3 python3-pip && apt-get install -y python3-venv

#creating a virtual environment and activating it 
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Installing the application in editable mode
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY heart_beat.py /app/heart_beat.py
COPY Schema.sql /docker-entrypoint-initdb.d/

WORKDIR /app

EXPOSE 5432

CMD ["python3", "heart_beat.py"]
