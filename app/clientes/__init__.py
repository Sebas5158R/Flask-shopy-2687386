from flask import Blueprint

clientes = Blueprint('clientes',
                     __name__,
                     url_prefix= '/clientes',
                     template_folder='templates')

# El punto es para importar todo lo que haya en routes
from . import routes