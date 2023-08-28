from app import db
from datetime import datetime

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

class Detalles(db.Model):
    __tablename__= "detalles"
    id= db.Column(db.Integer,primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id=db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)