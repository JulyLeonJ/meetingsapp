from app import app
from flask import render_template, redirect, request, session, session, flash
from model.reuniones import Reuniones


## ____________________________________________##


@app.route('/createreuniones',methods=['POST'])
def createreuniones():

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


@app.route('/showmeet/<int:id_reunion>')
def detail_pagemeet(id_reunion):
    data = {
        'id': id_reunion
    }
    return render_template("reunion.html",reuniones= reuniones.get_one(data))

## ________________________________________##


@app.route('/updatemeet/<int:id_reunion>', methods=['POST'])
def updatemeet(id_reunion):
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

@app.route('/deletemeet/<int:id_reunion>')
def deletemeet(id_reunion):
    data = {
        'id': id_reunion,
    }
    reuniones.destroy(data)
    return redirect('/reuniones')