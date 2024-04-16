import os
import dotenv
import rabbitmq_connector
import database_connector
import datetime
import threading
import json

dotenv.load_dotenv()

NODE_ID = os.getenv('NODE_ID')
NODE_NAME = os.getenv('NODE_NAME')
INTERVAL = os.getenv('INTERVAL')

RABBITMQ_QUEUE_HEALTH=os.getenv('RABBITMQ_QUEUE_HEALTH')
RABBITMQ_QUEUE_VALIDATION=os.getenv('RABBITMQ_QUEUE_VALIDATION')
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
        "node_name": NODE_NAME,
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
        send_heart_beat(producer)

"""
{'cart': [{'id': 1, 'name': 'P1', 'price': '10.00', 'quantity': 1, 'total': '10.00'}]}
{'cart': [{'id': 1, 'name': 'P1', 'price': '10.00', 'quantity': 2, 'total': 20}, {'id': 2, 'name': 'Pespi', 'price': '2.00', 'quantity': 2, 'total': 4}]}

"""


def add_order(cart,status="pending"):
    query = "INSERT INTO OrderDetails (order_date,status) VALUES (%s,%s) returning id"
    order_id = Database.execute_and_return(query,(datetime.datetime.now(),status))[0][0]

    query = "INSERT INTO OrderItems (order_id,product_id,quantity) VALUES (%s,%s,%s,%s)"
    for item in cart:
        Database.execute(query,(order_id,item['id'],item['quantity']))
    
    if status == "Success":
        total_price = sum(map(lambda x: int(x['total']),cart))

    pass




def validate_order(order):
    cart = order['cart']
    products = []
    for item in cart:
        products.append(item['id'])

    query = "SELECT id, quantity,price FROM products WHERE id IN (%s)"

    database_data = Database.execute_and_return(query,(','.join([str(k) for k in products]),))

    valid_items = []
    invalid_items = [] 
    for item in cart:
        for db_item in database_data:
            if db_item[0] == item['id']:
                if db_item[1] >= item['quantity']:
                    valid_items.append(item)
                else:
                    invalid_items.append(item)
                break
        pass

    if len(invalid_items) > 0:
        add_order(cart,status="Failed")
    else:
        add_order(cart,status="Success")

    
    return True


if __name__ == "__main__":
    Consumer=rabbitmq_connector.Connector(port=RABBITMQ_PORT,queue=RABBITMQ_QUEUE_VALIDATION,host=RABBITMQ_HOST)
    Database=database_connector.DatabaseConnector(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASS,database=DB_NAME)
    try:
        #th = threading.Thread(target=life)
        #th.start() 
        Consumer.consume(validate_order)
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
