import os
import dotenv
import rabbitmq_connector
import database_connector
import datetime
import threading
import json
import time

dotenv.load_dotenv()

NODE_ID = os.getenv('NODE_ID')
NODE_NAME = os.getenv('NODE_NAME')
INTERVAL = os.getenv('INTERVAL')

RABBITMQ_QUEUE_HEALTH=os.getenv('RABBITMQ_QUEUE_HEALTH')
RABBITMQ_QUEUE_PRODUCT=os.getenv('RABBITMQ_QUEUE_PRODUCT')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')


DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')


def send_heart_beat(mq_connection):
    channel = mq_connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE_HEALTH)

    data = { 
        "id": NODE_ID,
        "node": NODE_NAME,
        "checkpoint": str(datetime.datetime.now()),
    }
    try:
        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE_HEALTH, body=json.dumps(data))
    except Exception as e:
        print(e)
    pass

def life():
    producer = rabbitmq_connector.Connector(port=RABBITMQ_PORT,queue=RABBITMQ_QUEUE_HEALTH,host=RABBITMQ_HOST)
    while True:
        time.sleep(int(INTERVAL))
        send_heart_beat(producer)


def create_update(detail):
    ops = detail['ops']
    try:
        if ops == 'add':
            query = "INSERT INTO products (name,price,quantity) VALUES (%s,%s,%s) "
            Database.execute(query,(detail['name'],detail['price'],detail['quantity']))        
            Database.connection.commit()
            pass
        elif ops == 'update':
            query = "UPDATE products SET quantity=%s WHERE id=%s"
            Database.execute(query,(detail['quantity'],detail['id']))
            Database.connection.commit()
            pass
    except Exception as e:
        print(e)
        Database.connection.rollback()
        return False
    
    return True


if __name__ == "__main__":
    Consumer=rabbitmq_connector.Connector(port=RABBITMQ_PORT,queue=RABBITMQ_QUEUE_PRODUCT,host=RABBITMQ_HOST)
    Database=database_connector.DatabaseConnector(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASS,database=DB_NAME)
    try:
        #th = threading.Thread(target=life)
        #th.start() 
        Consumer.consume(create_update)
        #th.join()
    except KeyboardInterrupt as e:
        print("Exiting")
        Consumer.connection.close()
        Database.connection.close()
    except Exception as e:
        print(e)
        Consumer.connection.close()
        Database.connection.close()
    pass
