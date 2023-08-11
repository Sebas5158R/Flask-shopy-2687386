#importaciones del proyecto
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric( precision = 10, scale = 2 ))
    imagen = db.Column(db.String(120), unique = True)

class Ventas(db.Model):
    __tablename__= "ventas"
    id= db.Column(db.Integer,primary_key=True)
    fecha= db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id=db.Column(db.Integer, db.ForeignKey('clientes.id'))
