from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField

class LoginForm(FlaskForm):
    user_name = StringField('Nombre de usuario:')
    password = PasswordField('Contraseña:')
    submit = SubmitField('Iniciar sesión') 