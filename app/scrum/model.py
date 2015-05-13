

# Configuracion de la base de datos a utilizar.

import settings

from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey


db = declarative_base()

# Tablas de la base de datos a definir.


# Ojetivos

class Objetivo(db):
    
    __tablename__ = 'dpt'
    idobjetivo = Column(Integer, primary_key = True)
    descripcionobjetivo = Column(String(50), unique = True)
    users = relationship('User', backref = 'pila', cascade="all, delete, delete-orphan")

    def __init__(self, idobjetivo, descripcionobjetivo):
        self.idobjetivo = idobjetivo
        self.descripcionobjetivo = descripcionobjetivo

        

# Se crea el motor que almacenara los datos en el directorio local.
engine = create_engine(URL(**settings.DATABASE))    

#Se eliminnan las tablas anteriormente definidas
db.metadata.drop_all(engine)

# Se crean todas las tablas definidas en el motor antes construidos.
db.metadata.create_all(engine)
