from flask import render_template, redirect, url_for
from app.productos import productos
import app
import os
from .forms import NewProductForm

# Rutas
@productos.route('/create', methods = ['GET', 'POST'])
def crear():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        # Subir imagen a carpeta de imagenes
        # Campo de imagen (filestorage)
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + '/app/productos/imagenes/' + p.imagen))
        return redirect(url_for('productos.crear'))
    return render_template('new.html', form = form)


@productos.route('/update')
def actualizar():
    return 'Aqui vamos a actualizar información de productos'


@productos.route('/delete')
def eliminar():
    return 'Aqui vamos a eliminar productos'