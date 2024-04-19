# Imports
import pika
import os
import time
import dotenv
import json
import datetime


# Load environment variables
dotenv.load_dotenv()


# Get environment variables
NODE_ID = os.getenv('NODE_ID')
NODE_NAME = os.getenv('NODE_NAME')

RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE_HEALTH')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')

INTERVAL = os.getenv('INTERVAL')


def send_heart_beat(mq_connection):
    channel = mq_connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)

    data = {
        "id": NODE_ID,
        "node": NODE_NAME,
        "checkpoint": str(datetime.datetime.now()),
    }
    try:
        channel.basic_publish(
            exchange='', routing_key=RABBITMQ_QUEUE, body=json.dumps(data))
    except Exception as e:
        print(e)
    pass


if __name__ == "__main__":
    try:
        mq_connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        print("Heart beat service started")
        while True:
            send_heart_beat(mq_connection)
            time.sleep(int(INTERVAL))
    except KeyboardInterrupt as e:
        print("Exiting")
        mq_connection.close()
    except Exception as e:
        print(e)
        mq_connection.close()
