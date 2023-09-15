from flask import Flask, render_template
from flask_login import LoginManager
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import clientes
from app.auth import auth
from flask_bootstrap import Bootstrap

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

# Objeto para bootstrap
bootstrap = Bootstrap(app)

# Login
login = LoginManager(app)
login.login_view = "/auth/login"

#iniciacializar a continuacion el objeto SQLalchemy
db=SQLAlchemy(app)
Migrate(app , db)

# Registrar modulos (blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)
app.register_blueprint(auth)

# Toca importarlo desde aquí porque si no sale error
from .models import Cliente, Producto, Ventas, Detalles 

@app.route('/prueba')
def prueba():
    return render_template('base.html')