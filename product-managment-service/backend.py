import database_connector
import os
import dotenv
import json
import time

dotenv.load_dotenv()


Database = database_connector.DatabaseConnector(host=os.getenv('DB_HOST'), port=os.getenv(
    'DB_PORT'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), database=os.getenv('DB_NAME'))


def get_empty_stock():
    query = "SELECT * FROM products WHERE quantity = 0"
    return Database.execute_and_return(query, ())


def get_failed_orders():
    query = "SELECT id,order_date,total FROM orderdetails WHERE status = 'Failed'"
    return Database.execute_and_return(query, ())


def get_success_stock():
    query = "SELECT id,order_date,total FROM orderdetails WHERE status = 'Success'"
    return Database.execute_and_return(query, ())


def get_product():
    query = "SELECT * FROM products"
    return Database.execute_and_return(query, ())


def restock_product(product_id, quantity, mq_connection):
    data = {
        'ops': 'update',
        'id': product_id,
        'quantity': quantity
    }
    mq_connection.produce(data)

    pass


def add_new_product(name, quantity, price, mq_connection):
    data = {
        'ops': 'add',
        'name': name,
        'quantity': quantity,
        'price': price
    }
    mq_connection.produce(data)

    pass


def get_report():
    data = {}
    query = "SELECT invested,revenue FROM data_report "
    data["report"] = Database.execute_and_return(query, ())[0]
    query = "SELECT count(*) FROM orderdetails"
    data["orders"] = int(Database.execute_and_return(query, ())[0][0])
    query = "SELECT sum(quantity) FROM products"
    data["products"] = int(Database.execute_and_return(query, ())[0][0])
    return data


def heartbeat(mq_connection):
    data = {
        "id": os.getenv('NODE_ID'),
        "node": os.getenv('NODE_NAME'),
    }
    channel = mq_connection.channel()
    channel.queue_declare(queue=os.getenv('RABBITMQ_QUEUE_HEALTH'))
    while True:
        time.sleep(int(os.getenv('INTERVAL')))
        try:
            channel.basic_publish(exchange='', routing_key=os.getenv(
                'RABBITMQ_QUEUE_HEALTH'), body=json.dumps(data))
        except Exception as e:
            print(e)
