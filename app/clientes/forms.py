from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class ClientForm():
    user_name = StringField("Nombre:", validators = [InputRequired(message='Este campo es obligatorio')])
    email = EmailField("Email:", validators = [InputRequired(message='Este campo es obligatorio'), 
                                               Email(message='Debe ser un correo valido')])
    password = PasswordField("Contraseña:", validators=[InputRequired(message='Este campo es obligatorio'), 
                                                        Length(min=8, max=20, message='La contraseña debe tener min. 8 caracteres y max. 20')],
                             render_kw={"placeholder": "Nueva contraseña"})
    
    
class NewClienteForm(FlaskForm, ClientForm):
    submit = SubmitField("Registrar")
    

class EditCliente(FlaskForm, ClientForm):
    submit = SubmitField("Guardar")