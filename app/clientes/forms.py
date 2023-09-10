from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class ClientForm():
    user_name = StringField("Nombre:", validators = [InputRequired(message='Este campo es obligatorio')])
    email = EmailField("Email:", validators = [InputRequired(message='Este campo es obligatorio')])
    password = PasswordField("Contraseña:", validators=[InputRequired(message='Este campo es obligatorio')],
                             render_kw={"placeholder": "Nueva contraseña"})
    
    
class NewClienteForm(FlaskForm, ClientForm):
    submit = SubmitField("Registrar")
    

class EditCliente(FlaskForm, ClientForm):
    submit = SubmitField("Guardar")