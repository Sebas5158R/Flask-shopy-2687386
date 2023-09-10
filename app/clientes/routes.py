from flask import render_template, redirect, url_for, flash
from app.clientes import clientes
import app
from .forms import NewClienteForm, EditCliente

# Rutas
@clientes.route('/create', methods = ['GET', 'POST'])
def crear():
    c = app.models.Cliente()
    form = NewClienteForm()
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        
        flash('Cliente registrado con éxito')
        return redirect(url_for('clientes.listar'))
    return render_template('new_cliente.html', form = form)


@clientes.route('/listar')
def listar():
    clientes = app.models.Cliente.query.all()
    return render_template("listar_clientes.html", clientes = clientes)


@clientes.route('/update/<id_cliente>', methods = ['GET', 'POST'])
def actualizar(id_cliente):
    c = app.models.Cliente.query.get(id_cliente)
    form = EditCliente(obj = c)
    
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.commit()
        flash(f'Cliente {id_cliente} actualizado con éxito')
        return redirect(url_for('clientes.listar'))
    return render_template('new_cliente.html', form = form, c = c)


@clientes.route('/delete/<id_cliente>', methods = ['GET', 'POST'])
def eliminar(id_cliente):
    id_cliente = app.models.Cliente.query.get(id_cliente)
    eliminar = id_cliente
    if eliminar:
        app.db.session.delete(eliminar)
        app.db.session.commit()
        flash(f'Cliente {id_cliente} eliminado')
        return redirect(url_for('clientes.listar'))
    return render_template('listar_clientes.html')