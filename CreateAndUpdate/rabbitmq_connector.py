import pika
import json

class Connector:
        def __init__(self, port:int,queue:str,host:str="localhost") -> None:
            self.queue=queue
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port))
    
        def consume(self, user_callback):
            channel = self.connection.channel()

            channel.queue_declare(self.queue)

            def callback(ch, method, properties, body):
                user_callback(json.loads(body))

            channel.basic_consume(queue=self.queue, on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        def produce(self,data:dict):
                channel = self.connection.channel()

                channel.queue_declare(self.queue)

                try:
                      channel.basic_publish(exchange='', routing_key=self.queue, body=json.dumps(data))
                      print("Sent ",data)
                except Exception as e:
                      print(e)
                      return