from app import app
from flask import render_template, redirect, request, session, session, flash
from model.usuarios import Usuarios


## ____________________________________________##



@app.route('/createusuarios')
def createusuarios():
        
    data = {  ## data sera igual al nombre del metodo que estoy consumiendo del controlador
        "id_usuario":request.form['id_usuario'],
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
            }
    Usuarios.save(data)
    
    return redirect('/usuarios') 

## ________________________________________##

@app.route('/usuarios')
def usuarios():
    return render_template("usuarios.html",all_usuarios= Usuarios.get_all())

## ________________________________________##


@app.route('/showuser/<int:id_usuario>')
def detail_pageuser(id_usuario):
    data = {
        'id': id_usuario
    }
    return render_template("usuarios.html",usuarios= Usuarios.get_one(data))

## ________________________________________##


@app.route('/updateuser/<int:id_usuario>', methods=['POST'])
def updateuser(id_usuario):
    data = {
        'id': id_usuario,
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
    }
    Usuarios.update(data)
    return redirect(f"/show/{id_usuario}")

## ________________________________________##

@app.route('/deleteuser/<int:id_usuario>')
def deleteuser(id_usuario):
    data = {
        'id': id_usuario,
    }
    Usuarios.destroy(data)
    return redirect('/usuarios')