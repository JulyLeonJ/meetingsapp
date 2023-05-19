from meetingsapp import app
from flask import render_template, redirect, request, session, session, flash
from model import usuarios

@app.route('/')
def index():
    return render_template("home.html")

## ____________________________________________##



@app.route('/create',methods=['POST'])
def create():
        
    data = {
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
            }
    usuarios.save(data)
    
    return redirect('/usuarios')

## ________________________________________##

@app.route('/usuarios')
def usuarios():
    return render_template("usuarios.html",all_usuarios= usuarios.get_all())

## ________________________________________##


@app.route('/show/<int:id_usuario>')
def detail_page(id_usuario):
    data = {
        'id': id_usuario
    }
    return render_template("usuario.html",usuarios= usuarios.get_one(data))

## ________________________________________##

@app.route('/edit_page/<int:id_usuario>')
def edit_page(id_usuario):
    data = {
        'id': id_usuario
    }
    return render_template("edit_page.html", usuario = usuarios.get_one(data))

## ________________________________________##

@app.route('/update/<int:id_usuario>', methods=['POST'])
def update(id_usuario):
    data = {
        'id': id_usuario,
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
    }
    usuarios.update(data)
    return redirect(f"/show/{id_usuario}")

## ________________________________________##

@app.route('/delete/<int:id_usuario>')
def delete(id_usuario):
    data = {
        'id': id_usuario,
    }
    usuarios.destroy(data)
    return redirect('/usuarios')