from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField 
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed 

class NewProductForm(FlaskForm):
    nombre = StringField("Nombre producto:", validators = [InputRequired(message= 'Este campo es obligatorio')])
    precio = IntegerField("Precio del producto:", validators = [
        InputRequired(message= 'Este campo es obligatorio'),
        NumberRange(message= 'Precio fuera de rango', min=800, max=100000)
        ])
    imagen = FileField(label = "Imagen del producto", validators = [FileRequired(message='Se requiere una imagen'), 
                                                                    FileAllowed(['jpg', 'png'], message='Archivo no permitido')])
    submit = SubmitField("Registrar producto")