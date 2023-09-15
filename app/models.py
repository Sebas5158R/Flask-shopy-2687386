from app import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

#modelos - entidades del proyecto
class Cliente(db.Model ,UserMixin):
    # Creando las columnas de la base de datos
    __tablename__ = "clientes" # Nombre que va a tener la tabla
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(128))
    email= db.Column(db.String(100), unique = True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password = password)
    
    def check_password(self, password):
        return check_password_hash ( self.password, password )
    
@login.user_loader
def load_user(id):
    return Cliente.query.get(id)


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