from index import app
from flask import render_template, redirect, request, session, session, flash
from model.reuniones import Reuniones

@app.route('/')
def index():
    return render_template("home.html")

## ____________________________________________##


@app.route('/create',methods=['POST'])
def create():

    data = {
        "titulo":request.form['titulo'],
        "duracion":request.form['duracion'],
        "lugar": request.form['lugar'],
        "organizador": request.form['organizador'],
        "hora":request.form['hora'],
        "disponibilidad": request.form['disponibilidad'],
        "id_invitado": request.form['id_invitado'],
        
            }
    reuniones.save(data)
    
    return redirect('/reuniones')

## ________________________________________##

@app.route('/reuniones')
def reuniones():
    return render_template("reuniones.html",all_reuniones= reuniones.get_all())

## ________________________________________##


@app.route('/show/<int:id_reunion>')
def detail_page(id_reunion):
    data = {
        'id': id_reunion
    }
    return render_template("reunion.html",reuniones= reuniones.get_one(data))

## ________________________________________##

@app.route('/edit_page/<int:id_reunion>')
def edit_page(id_reunion):
    data = {
        'id': id_reunion
    }
    return render_template("edit_page.html", reunion = reuniones.get_one(data))

## ________________________________________##

@app.route('/update/<int:id_reunion>', methods=['POST'])
def update(id_reunion):
    data = {
        "titulo":request.form['titulo'],
        "duracion":request.form['duracion'],
        "lugar": request.form['lugar'],
        "organizador": request.form['organizador'],
        "hora":request.form['hora'],
        "disponibilidad": request.form['disponibilidad'],
        "id_invitado": request.form['id_invitado'],
    }
    reuniones.update(data)
    return redirect(f"/show/{id_reunion}")

## ________________________________________##

@app.route('/delete/<int:id_reunion>')
def delete(id_reunion):
    data = {
        'id': id_reunion,
    }
    reuniones.destroy(data)
    return redirect('/reuniones')