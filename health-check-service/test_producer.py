import rabbitmq_connector


connector=rabbitmq_connector.Connector(port=5672,queue="Test")

a=0
while True:
    connector.produce({"node":"Test{}".format(a),"status":False})
    a+=1
print("sent")
    