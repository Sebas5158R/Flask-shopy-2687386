from flask_login import login_user, current_user, logout_user
from flask import render_template, redirect, url_for, flash
from app.auth import auth
import app
from .forms import LoginForm


@auth.route('/login' , methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Se selecciona el cliente por user_name
        c = app.models.Cliente.query.filter_by(user_name = form.user_name.data).first()
        if c is None or not c.check_password(form.password.data):
            flash('Usuario no encontrado o contraseña invalida')
            return redirect('/auth/login')
        else:
            login_user(c, remember = True)
            return redirect('/productos/listar')
    return render_template('login.html', form = form)

@auth.route('/logout' , methods = ['GET'])
def logout():
    logout_user()
    flash('Sesión cerrada exitosamente')
    return redirect('/auth/login')