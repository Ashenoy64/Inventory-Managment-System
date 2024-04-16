import database_connector
import os
import dotenv
import json
import time

dotenv.load_dotenv()


Database = database_connector.DatabaseConnector(host=os.getenv('DB_HOST'),port=os.getenv('DB_PORT'),user=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),database=os.getenv('DB_NAME'))  


def get_empty_stock():
    query = "SELECT id,quantity FROM products WHERE quantity = 0"
    return Database.execute_and_return(query,())

def get_failed_orders():
    query = "SELECT id,cart FROM orders WHERE status = 'Failed'"
    return Database.execute_and_return(query,())

def restock_product(product_id,quantity):
    query = "UPDATE products SET quantity = quantity + %s WHERE id = %s"
    Database.execute(query,(quantity,product_id))

def get_product():
    query = "SELECT id,quantity,price FROM products"
    return Database.execute_and_return(query,())

def add_new_product(name,quantity,price):
    query = "INSERT INTO products(name,quantity,price) VALUES (%s,%s,%s) RETURNING id"
    try:
        Database.execute(query,(name,quantity,price))[0][0]  
        Database.connection.commit() 
        return True
    except Exception as e:
        print(e)
        Database.connection.rollback()  
        return False




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
            channel.basic_publish(exchange='', routing_key=os.getenv('RABBITMQ_QUEUE_HEALTH'), body=json.dumps(data))
        except Exception as e:
            print(e)
    

    