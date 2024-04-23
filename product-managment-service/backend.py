import database_connector
import os
import dotenv
import json
import time
import datetime
import rabbitmq_connector
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


def restock_product(product_id, quantity,price, mq_connection):
    data = {
        'ops': 'update',
        'id': product_id,
        'quantity': quantity,
        'cost': price,
        'price': round(price * (1+float(os.getenv('PROFIT_MARGIN'))),1),
    }
    mq_connection.produce(data)

    pass


def get_order_count():
    query = "SELECT order_date,count(*) FROM orderdetails GROUP BY order_date"
    return Database.execute_and_return(query, ())

def get_product_count():
    query = "SELECT  name,sum(orderitems.quantity) FROM products JOIN orderitems ON products.id = orderitems.product_id GROUP BY name"
    return Database.execute_and_return(query, ())

def add_new_product(name, quantity, price, mq_connection):
    data = {
        'ops': 'add',
        'name': name,
        'quantity': quantity,
        'cost': price,
        'price': round(price * (1+float(os.getenv('PROFIT_MARGIN'))),1),
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


def heartbeat():
    producer = rabbitmq_connector.Connector(port=os.getenv("RABBITMQ_PORT"),queue=os.getenv("RABBITMQ_QUEUE_HEALTH"),host=os.getenv("RABBITMQ_HOST"))
    data = {
        "id": os.getenv('NODE_ID'),
        "node": os.getenv('NODE_NAME'),
        "checkpoint": str(datetime.datetime.now()),
    }   
    while True:
        time.sleep(int(os.getenv('INTERVAL')))
        try:
            print("Sending Heartbeat")
            producer.produce(data)
        except Exception as e:
            print(e)
