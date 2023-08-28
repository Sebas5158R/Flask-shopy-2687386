from flask import Blueprint

productos = Blueprint('productos',
                      __name__,
                      url_prefix= "/productos",
                      template_folder= 'templates')

# El punto es para importar todo lo que haya en routes
from . import routes