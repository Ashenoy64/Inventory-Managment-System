import database_connector
import rabbitmq_connector



Consumer=rabbitmq_connector.Connector(port=5672,queue="Test")
Database=database_connector.Connector(database="Test")




def process_message(boady):
    print(boady)
    Database.insert(boady["node"],boady["status"])



Consumer.consume(process_message)
