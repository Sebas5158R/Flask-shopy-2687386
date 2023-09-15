from flask import Blueprint

auth = Blueprint('auth',
                      __name__,
                      url_prefix= "/auth",
                      template_folder= 'templates')

# El punto es para importar todo lo que haya en routes
from . import routes