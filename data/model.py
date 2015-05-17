

# Configuracion de la base de datos a utilizar.

import data.settings

from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey


db = declarative_base()

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

num_pila = 0
num_acciones = 0
num_actores = 0
num_objetivos = 0

# Tabla Pila (Productos):
class Pila(db):
    __tablename__   = 'pila'
    idPila          = Column(Integer, primary_key = True)
    nomProducto     = Column(String(30), nullable = True)
    idActor         = Column(Integer, nullable = True)
    nomActor        = Column(String(500), nullable = True)
    idObjetivo      = Column(Integer, nullable = True)
    descripObjetivo = Column(String(500), nullable = True)
    idAccion        = Column(Integer, nullable = True)
    descripAccion   = Column(String(500), nullable = True)

    def __init__(self,nomProducto,idActor,nomActor, idObjetivo, descripObjetivo, idAccion, descripAccion):
        num_pila     = num_pila + 1
        self.idPila  = num_pila
        self.nomProducto = nomProducto
        self.idActor = idActor
        self.nomActor = nomActor
        self.idObjetivo = idObjetivo
        self.descripObjetivo = descripObjetivo
        self.idAccion = idAccion
        self.descripAccion = descripAccion

# Tabla Usuario.
class User(db):
    __tablename__ = 'usuario'
    fullname = Column(String(50), nullable = False)
    username = Column(String(16), primary_key = True)
    password = Column(String(16), nullable = False)
    email    = Column(String(30), unique = True)
    #idActores = Column(Integer, ForeignKey('actores.idactores'))

    def __init__(self,fullname, username, password, email):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        #self.idAcciones = idAcciones


# Tabla Acciones.
class Acciones(db):
    __tablename__ = 'acciones'
    idacciones      = Column(Integer, primary_key = True)
    descripAcciones = Column(String(500), nullable = False)
    #usuarios       = relationship('User', backref = 'acciones', cascade="all, delete, delete-orphan")
    #pilas = relationship('Pila', backref = 'acciones', cascade="all, delete, delete-orphan")

    def __init__(self, idacciones, descripAcciones):
        # Constructor del modelo Acciones.
        num_acciones         = num_acciones + 1
        self.idacciones      = num_acciones
        self.descripAcciones = descripAcciones


# Tabla Actores.
class Actores(db):
    __tablename__ = 'actores'
    id_actores     = Column(Integer, primary_key = True)
    nombre_actores = Column(String(50), nullable = False)
    #pilas = relationship('Pila', backref = 'acciones', cascade="all, delete, delete-orphan")

    def __init__(self, nombre_actores):
        # Constructor del modelo Acciones.
        num_actores          = num_actores + 1
        self.id_actores      = num_actores
        self.nombre_actores  = nombre_actores
        
class Objetivos(db):
    __tablename__ = 'objetivos'
    id_objetivos   = Column(Integer, primary_key = True)
    descripObjetivos = Column(String(500), nullable = False)
    
    def __init(self,descripObjetivos):
        num_objetivos          = num_objetivos + 1
        self.id_objetivos      = num_objetivos
        self.descripObjetivos  = descripObjetivos
        
#-------------------------------------------------------------------------------

# Se crea el motor que almacenara los datos en el directorio local.
engine = create_engine(URL(**data.settings.DATABASE))    

#Se eliminnan las tablas anteriormente definidas
db.metadata.drop_all(engine)

# Se crean todas las tablas definidas en el motor antes construidos.
db.metadata.create_all(engine)

