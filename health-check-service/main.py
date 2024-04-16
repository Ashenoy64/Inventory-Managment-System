import database_connector
import rabbitmq_connector
import datetime
import Settings
import threading
import time

Consumer=rabbitmq_connector.Connector(port=Settings.RABBITMQ["PORT"],queue=Settings.RABBITMQ["QUEUE"],host=Settings.RABBITMQ["HOST"])
Database=database_connector.Connector()




def process_message(body):
    Database.upsert(body['id'],body["node"],datetime.datetime.strptime(body['checkpoint'], '%Y-%m-%d %H:%M:%S.%f'))


def self_heartbeat():
    while True:
        time.sleep(Settings.NODE["INTERVAL"])
        Database.upsert(Settings.NODE['ID'],Settings.NODE['NAME'],datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f'))

try:
    th = threading.Thread(target=self_heartbeat)
    th.start()
    Consumer.consume(process_message)
    th.join()
except KeyboardInterrupt as e:
    print("Exiting...")
except Exception as e:
    print(e)