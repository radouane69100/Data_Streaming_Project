# Importation des modules nécessaires pour interagir avec la base de données
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from models import Base
# Importation de la configuration de la base de données depuis le fichier .env
from dotenv import dotenv_values, load_dotenv

load_dotenv()

CONFIG = dotenv_values("class-4/.env")

# creation d'un moteur SQLAlchemy et renvoi d'une session pour interagir avec la base de données
def CreateEngine():
    engine = create_engine("mysql+mysqlconnector://%s:%s@%s:%s/%s" %    # Création du moteur SQLAlchemy avec les informations de la base de données issues du fichier .env
                           (CONFIG['MYSQL_USER'],
                            CONFIG['MYSQL_PASSWORD'], CONFIG['HOST'],CONFIG['PORT'],CONFIG['MYSQL_DATABASE'])
                           )


    connection = engine.connect()
    ## Création des tables dans la base de données
    Base.metadata.create_all(engine)
    # Création d'une session pour interagir avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # Renvoi de la session créée
    return session