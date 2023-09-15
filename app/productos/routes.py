from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.productos import productos
import app
import os
from .forms import NewProductForm, EditProductForm

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
@login_required
def listar():
    productos = app.models.Producto.query.all()
    return render_template("listar.html", productos = productos)

@productos.route('/update/<id_producto>', methods = ['GET', 'POST'])
def actualizar(id_producto):
    p = app.models.Producto.query.get(id_producto)
    form = EditProductForm(obj = p)
    
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash(f'Producto {id_producto} editado con éxito')
        return redirect(url_for('productos.listar'))
    return render_template('new.html', form = form, p = p)


@productos.route('/delete/<id_producto>', methods = ['GET', 'POST'])
def eliminar(id_producto):
    id_producto = app.models.Producto.query.get(id_producto)
    eliminar = id_producto
    if eliminar:
        app.db.session.delete(eliminar)
        app.db.session.commit()
        flash(f'Producto {id_producto} eliminado')
        return redirect(url_for('productos.listar'))
    return 'Aqui vamos a eliminar productos con el id ' + id_producto