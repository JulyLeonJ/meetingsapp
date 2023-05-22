from app import app
from flask import render_template, redirect, request, session, session, flash
from model.invitados import Invitados


## ____________________________________________##



@app.route('/createinvitados',methods=['POST'])
def createinvitados():

    data = {
        "disponibilidad": request.form['disponibilidad'],
        "id_invitado": request.form['id_invitado'],
        
            }
    invitados.save(data)
    
    return redirect('/invitados')

## ________________________________________##

@app.route('/invitados')
def invitados():
    return render_template("invitados.html",all_invitados= invitados.get_all())

## ________________________________________##


@app.route('/showguest/<int:id_invitado>')
def detail_pageguest(id_invitado):
    data = {
        'id': id_invitado
    }
    return render_template("invitados.html",invitados= invitados.get_one(data))

## ________________________________________##


@app.route('/updateguest/<int:id_invitado>', methods=['POST'])
def updateguest(id_invitado):
    data = {
        "disponibilidad": request.form['disponibilidad'],
        "id_invitado": request.form['id_invitado'],
    }
    invitados.update(data)
    return redirect(f"/show/{id_invitado}")

## ________________________________________##

@app.route('/deleteguest/<int:id_invitado>')
def deleteguest(id_invitado):
    data = {
        'id': id_invitado,
    }
    invitados.destroy(data)
    return redirect('/invitados')