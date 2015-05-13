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

from flask					import Flask
from flask.ext.migrate		import Migrate, MigrateCommand
from flask.ext.sqlalchemy  	import SQLAlchemy
from flask.ext.script		import Manager
from sqlalchemy 			import CheckConstraint

#-------------------------------------------------------------------------------

# Construcción de la base de datos.

SQLALCHEMY_DATABASE_URI = "postgresql://BMO:@localhost/newapmwsc"
	# Estructura para realizar la conexión con la base de datos:
	# "postgresql://yourusername:yourpassword@localhost/yournewdb"

db_dir = 'postgresql+psycopg2://BMO:@localhost/newapmwsc'
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

# Tabla Acciones.
class Acciones(db.Model):
	__tablename__ = 'acciones'
	idacciones 		= db.Column(db.Integer, primary_key = True)
	descripAcciones = db.Column(db.String(50), nullable = False)
	#pilas = relationship('Pila', backref = 'acciones', cascade="all, delete, delete-orphan")

	def __init__(self, idacciones, descripAcciones):
		# Constructor del modelo Acciones.
		self.idacciones 	 = idacciones
		self.descripAcciones = descripAcciones
		

#-------------------------------------------------------------------------------
def createDatabase():
	db.create_all()

if __name__ == '__main__':
	# Se crean las tablas de la base de datos.
	createDatabase()
	manager.run()