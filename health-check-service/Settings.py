import os 
import dotenv

dotenv.load_dotenv()


DATABASES = {
    'default': {
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

RABBITMQ = {
    'HOST': os.getenv('RABBITMQ_HOST'),
    'PORT': os.getenv('RABBITMQ_PORT'),
    'QUEUE': os.getenv('RABBITMQ_QUEUE'),
}


NODE ={
    'ID': os.getenv('NODE_ID'),
    'NAME': os.getenv('NODE_NAME'),
    'INTERVAL': int(os.getenv('INTERVAL')),
}