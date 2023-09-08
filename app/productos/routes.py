from flask import render_template, redirect, url_for, flash
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
        
        flash('Producto registrado con éxito')
        return redirect(url_for('productos.listar'))
    return render_template('new.html', form = form)


@productos.route('/listar')
def listar():
    productos = app.models.Producto.query.all()
    return render_template("listar.html", productos = productos)

@productos.route('/update/<id_producto>', methods = ['GET', 'POST'])
def actualizar(id_producto):
    return 'Aqui vamos a actualizar información de productos con el id ' + id_producto


@productos.route('/delete/<id_producto>', methods = ['GET', 'POST'])
def eliminar(id_producto):
    return 'Aqui vamos a eliminar productos con el id ' + id_producto