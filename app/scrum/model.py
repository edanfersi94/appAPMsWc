# -*- coding: utf-8 -*-. 

"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        Equipo SoftDev
    DESCRIPCION: 
        
"""
#-------------------------------------------------------------------------------

# Librerias a importar.

from flask                  import Flask
from flask.ext.migrate      import Migrate, MigrateCommand
from flask.ext.sqlalchemy   import SQLAlchemy
from flask.ext.script       import Manager
from sqlalchemy             import CheckConstraint

#-------------------------------------------------------------------------------

# Construcción de la base de datos.

SQLALCHEMY_DATABASE_URI = "postgres://postgres:joel123:@localhost/JyA-USB2"
    # Estructura para realizar la conexión con la base de datos:
    # "postgresql://yourusername:yourpassword@localhost/yournewdb"

db_dir = 'postgresql+psycopg2://postgres:joel123@localhost/JyA-USB2'
# Estructrua:
# 'postgresql+psycopg2://user:password@localhost/the_database'  

# Instancia de la aplicación a utilizar.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_dir
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# Instancia de la base de datos a usar.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#-------------------------------------------------------------------------------

# Tablas de la base de datos a definir.

# Tabla Objetivo
class Objetivo(db.Model):
    __tablename__ = 'objetivo'
    idObjetivo    = db.Column(db.Integer, primary_key = True)
    descripObjetivo = db.Column(db.String(50), nullable = False)
    #pilas = relationship('Pila', backref = 'objetivo', cascade="all, delete, delete-orphan")

    def __init__(self, idobjetivo, descripObjetivo):
        # Constructor del modelo Acciones.
        self.idObjetivo      = idObjetivo
        self.descripObjetivo  = descripObjetivo
        

#-------------------------------------------------------------------------------
def createDatabase():
    db.create_all()

if __name__ == '__main__':
    # Se crean las tablas de la base de datos.
    createDatabase()
    manager.run()