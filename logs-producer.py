import time

from server import channel

#Ouverture du fichier de logs
logs_files = open("class-4/assets/web-server-nginx.log", "r")

#Définition des queues à créer
QUEUES = [
    {
        "name": "queue-data-lake",
        "routing_key": "logs"
    },
    {
        "name": "queue-data-clean",
        "routing_key": "logs"
    }
]

#Nom de l'exchange
EXCHANGE_NAME = "topic-exchange-logs"

# Création de l'exchange
channel.exchange_declare(EXCHANGE_NAME, durable=True, exchange_type='topic')

# creation des queues
for queue in QUEUES:
    channel.queue_declare(queue=queue['name'])
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue['name'], routing_key=queue['routing_key'])

# Publication des événements en boucle
for line in logs_files:

    # Pause de 0.05 secondes pour limiter le taux de publication
    time.sleep(0.05)
    # Publication de l'événement sur la queue
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key="logs", body=line)

    # Affichage d'un message de confirmation pour chaque événement publié
    print(f"[x] published event `{line}` in topic `{queue['routing_key']}`")