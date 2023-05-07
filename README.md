# Data_Streaming_Project

OBJECTIF: 

Mettre en place un flux data qui récupère les logs d'un server web les traites et les insères dans une base de données.

Pour cela on crée un système d'analyse des logs qui récupère les logs d'un serveur web en temps réel, qui se base sur  un logs-producer, utilise RabbitMq comme Message Broker, récupère les logs dans deux consumers en fonction des traitements à accomplir puis les stocke dans une base de données mysql.




ARCHITECTURE MISEN EN PLACE:



![image](https://user-images.githubusercontent.com/115105703/236688102-45526cc2-c72a-4280-8474-4265d2cf1c76.png)





PREREQUIS:


    •	Python 3.x
    •	Docker
    •	Docker Compose
    




INSTALLATION:

- Cloner le repository:  
  git clone https://github.com/radouane69100/Data_Streaming_Project.git
  
- CD Data_Streaming_Project

- Créer et activer l'environnement virtuel:
  venv/Scripts/activate
  
- Installer les requirements:
  pip install -r requirements.txt
  
- Dupliquer le fichier .env.example et le modifier pour l'adapter à vos variables d'environnement



CONFIGURATION A METTRE EN PLACE:


- Lancer docker-compose:
  docker-compose up -d
  
  Le fichier docker-compose.yml configure trois services: RabittMQ, MySQL, PHPMyAdmin
  
  
EXECUTION:


 - Pour lancer le producer qui va lire les logs et les publier danss un échange RabittMQ, exécuter: 
          logs-producer.py
          
 - Pour consommer les logs et les traiter en temps réel et les stocker dans la bas de données MySQL::
          data-lake-consumer.py
          data-clean-consumer.py
