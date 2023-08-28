from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField

class NewProductForm(FlaskForm):
    nombre = StringField("Nombre producto:")
    precio = IntegerField("Precio del producto:")
    submit = SubmitField("Registrar producto")