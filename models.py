# importer les classes nécessaires pour la création de la base de données

from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Date, Text
from sqlalchemy.dialects.mysql import FLOAT as MY_SQL_FLOAT, JSON
from sqlalchemy.orm import DeclarativeBase

# la classe Base sert de base pour toutes les classes de modèle de base de données
class Base(DeclarativeBase):
    pass

# la classe CleanLog représente les données de logs nettoyées qui seront stockées dans la base de données
class CleanLog(Base):
    __tablename__ = "clean-log"

    # les colonnes représentent les différents champs des logs nettoyés qui seront stockés dans la base de données

    id = Column(String(255), primary_key=True, nullable=False)
    timestamp = Column(String(255), nullable=True)
    year = Column(String(255), nullable=True)
    month = Column(String(255), nullable=True)
    day = Column(String(255), nullable=True)
    day_of_week = Column(String(255), nullable=True)
    time = Column(String(255), nullable=True)
    ip = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    session = Column(String(255), nullable=True)
    user = Column(String(255), nullable=True)
    is_email = Column(String(255), nullable=True)
    email_domain = Column(String(255), nullable=True)
    rest_method = Column(String(255), nullable=True)
    url = Column(Text, nullable=True)
    schema = Column(String(255), nullable=True)
    host = Column(String(255), nullable=True)
    rest_session = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    status_verbose = Column(String(255), nullable=True)
    size_bytes = Column(String(255), nullable=True)
    size_kilo_bytes = Column(String(255), nullable=True)
    size_mega_bytes = Column(String(255), nullable=True)

# la classe RowLog représente les données de chaque ligne de log qui seront stockées dans la base de données
class RowLog(Base):
    __tablename__ = "row-log"

    # les colonnes représentent les différents champs des logs qui seront stockés dans la base de données
    id = Column(String(255),primary_key=True, nullable=False)
    timestamp = Column(String(255), nullable=False)
    log = Column(Text, nullable=False)