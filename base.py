# -*- coding: utf-8 -*-. 
from flask                  import Flask, request, session
from flask.ext.migrate      import Migrate, MigrateCommand
from flask.ext.sqlalchemy   import SQLAlchemy
from sqlalchemy             import CheckConstraint
from flask.ext.script       import Manager, Server
from random                 import SystemRandom
from datetime               import timedelta

app = Flask(__name__, static_url_path='')

SQLALCHEMY_DATABASE_URI = "postgresql://BMO:@localhost/newapmwsc"
    # Estructura para realizar la conexión con la base de datos:
    # "postgresql://yourusername:yourpassword@localhost/yournewdb"

db_dir = 'postgresql+psycopg2://BMO:@localhost/newapmwsc'
# Estructrua:
# 'postgresql+psycopg2://user:password@localhost/the_database'     

app.config['SQLALCHEMY_DATABASE_URI'] = db_dir
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

manager.add_command('db', MigrateCommand)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

from app.scrum.ident import ident
app.register_blueprint(ident)
from app.scrum.prod import prod
app.register_blueprint(prod)
from app.scrum.mast import mast
app.register_blueprint(mast)
from app.scrum.dev import dev
app.register_blueprint(dev)
from app.scrum.actor import actor
app.register_blueprint(actor)
from app.scrum.objetivo import objetivo
app.register_blueprint(objetivo)
from app.scrum.accion import accion
app.register_blueprint(accion)



#Application code starts here

# Tabla Acciones.
class Acciones(db.Model):
    __tablename__ = 'acciones'
    idacciones         = db.Column(db.Integer, primary_key = True)
    descripAcciones = db.Column(db.String(50), nullable = False)
    #pilas = relationship('Pila', backref = 'acciones', cascade="all, delete, delete-orphan")

    def __init__(self, idacciones, descripAcciones):
        # Constructor del modelo Acciones.
        self.idacciones      = idacciones
        self.descripAcciones = descripAcciones
        



#Application code ends here

if __name__ == '__main__':
    db.create_all()
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()

