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
RABBITMQ_QUEUE_VALIDATION=os.getenv('RABBITMQ_QUEUE_VALIDATION')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')


DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')


def send_heart_beat(mq_connection):
    data = { 
        "id": NODE_ID,
        "node": NODE_NAME,
        "checkpoint": str(datetime.datetime.now()),
    }
    try:
        mq_connection.produce(data)
    except Exception as e:
        print(e)
    pass

def life():
    producer = rabbitmq_connector.Connector(port=RABBITMQ_PORT,queue=RABBITMQ_QUEUE_HEALTH,host=RABBITMQ_HOST)
    while True:
        time.sleep(int(INTERVAL))
        send_heart_beat(producer)




def add_order(cart,status="pending"):
    try:
        total_price = sum(map(lambda x: float(x['total']),cart))
        query = "INSERT INTO OrderDetails (order_date,status,total) VALUES (%s,%s,%s) returning id"
        
        order_id = Database.execute_and_return(query,(datetime.datetime.now(),status,total_price))[0][0]

        add_query = "INSERT INTO OrderItems (order_id,product_id,quantity) VALUES (%s,%s,%s)"
        update_query = "UPDATE products SET quantity = quantity - %s WHERE id = %s"
        for item in cart:
            Database.execute(add_query,(order_id,item['id'],item['quantity']))
            Database.execute(update_query,(item['quantity'],item['id']))
        Database.connection.commit()
    except Exception as e:
        print(e)
        Database.connection.rollback()
        
    if status == "Success":
        query = "UPDATE DATA_REPORT SET revenue= revenue + %s "
        try:
            Database.execute(query,(total_price,))
            Database.connection.commit()
        except Exception as e:
            print(e)
            Database.connection.rollback()




def validate_order(order):
    cart = order['cart']
    products = []
    for item in cart:
        products.append(item['id'])

    query = "SELECT id, quantity, price FROM products WHERE id IN (%s)"
    placeholders = ','.join(['%s' for _ in products])
    database_data = Database.execute_and_return(query % placeholders, products)
    
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
        th = threading.Thread(target=life)
        th.start() 
        Consumer.consume(validate_order)
        th.join()
    except KeyboardInterrupt as e:
        print("Exiting")
        Consumer.connection.close()
        Database.connection.close()
    except Exception as e:
        print(e)
        Consumer.connection.close()
        Database.connection.close()
    pass
