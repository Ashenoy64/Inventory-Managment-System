import rabbitmq_connector
import datetime

connector=rabbitmq_connector.Connector(port=5672,queue="Test")

connector.produce({"id":1,"node":"node1","checkpoint":str(datetime.datetime.now())})
print("sent")
    