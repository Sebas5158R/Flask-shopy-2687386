#importaciones del proyecto
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)


#iniciacializar a continuacion el objeto SQLalchemy
db=SQLAlchemy(app)
Migrate(app , db)


#modelos - entidades del proyecto
class Cliente(db.Model):
    # Creando las columnas de la base de datos
    __tablename__ = "clientes" # Nombre que va a tener la tabla
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    email= db.Column(db.String(100), unique = True)