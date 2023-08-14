#importaciones del proyecto
from flask import Flask, render_template
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)


#iniciacializar a continuacion el objeto SQLalchemy
db=SQLAlchemy(app)
Migrate(app , db)

# Crear formulario de registro de clientes
class RegistroClienteForm(FlaskForm):
    user_name = StringField("Nombre de Usuario")
    email = StringField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Registrar")


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


@app.route('/clientes/create', 
           methods = ['GET', 'POST'])
def crear_cliente():
    # instanciar formulario
    form = RegistroClienteForm()
    if form.validate_on_submit():
        # crear el nuevo cliente
        c = Cliente(user_name = form.user_name.data, email = form.email.data, password = form.password.data)
        db.session.add(c)
        db.session.commit()
        return "Cliente registrado con éxito"
    return render_template('registro.html', form = form)


@app.route('/clientes',
           methods = ['GET'])
def listar_clientes():
    #seleccionar todos los clientes
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)