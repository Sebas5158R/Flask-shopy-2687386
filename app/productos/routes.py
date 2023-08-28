from flask import render_template
from app.productos import productos
from .forms import NewProductForm

# Rutas
@productos.route('/create')
def crear():
    form = NewProductForm()
    return render_template('new.html', form = form)


@productos.route('/update')
def actualizar():
    return 'Aqui vamos a actualizar información de productos'


@productos.route('/delete')
def eliminar():
    return 'Aqui vamos a eliminar productos'