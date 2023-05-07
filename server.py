import pika

from config import CONFIG

RABBIT_MQ_SERVER = "localhost"

# Etablissement d'une connexion avec RabbitMQ en utilisant les paramètres de connexion
credentials = pika.PlainCredentials(CONFIG['RABBIT_USER'], CONFIG['RABBIT_PASSWORD'])
parameters = pika.ConnectionParameters(RABBIT_MQ_SERVER, credentials=credentials,heartbeat=30)
connection = pika.BlockingConnection(parameters)

#Creation d'un canal de communication avec RabbitMQ sur la connexion établie
channel = connection.channel()

