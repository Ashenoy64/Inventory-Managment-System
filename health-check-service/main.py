import database_connector
import rabbitmq_connector
import datetime
Consumer=rabbitmq_connector.Connector(port=5672,queue="Test")
Database=database_connector.Connector()




def process_message(body):
    Database.upsert(body['id'],body["node"],datetime.datetime.strptime(body['checkpoint'], '%Y-%m-%d %H:%M:%S.%f'))

try:
    Consumer.consume(process_message)
except KeyboardInterrupt as e:
    print("Exiting...")
except Exception as e:
    print(e)