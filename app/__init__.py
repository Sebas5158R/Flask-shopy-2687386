from flask import Flask, render_template
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from flask_bootstrap import Bootstrap

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

# Objeto para bootstrap
bootstrap = Bootstrap(app)

#iniciacializar a continuacion el objeto SQLalchemy
db=SQLAlchemy(app)
Migrate(app , db)

# Registrar modulos (blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

# Toca importarlo desde aquí porque si no sale error
from .models import Cliente, Producto, Ventas, Detalles 

@app.route('/prueba')
def prueba():
    return render_template('base.html')