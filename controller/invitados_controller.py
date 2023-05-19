from index import app
from flask import render_template, redirect, request, session, session, flash
from model import invitados

@app.route('/')
def index():
    return render_template("home.html")

## ____________________________________________##



@app.route('/create',methods=['POST'])
def create():

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


@app.route('/show/<int:id_invitado>')
def detail_page(id_invitado):
    data = {
        'id': id_invitado
    }
    return render_template("invitado.html",invitados= invitados.get_one(data))

## ________________________________________##

@app.route('/edit_page/<int:id_invitado>')
def edit_page(id_invitado):
    data = {
        'id': id_invitado
    }
    return render_template("edit_page.html", invitado = invitados.get_one(data))

## ________________________________________##

@app.route('/update/<int:id_invitado>', methods=['POST'])
def update(id_invitado):
    data = {
        "disponibilidad": request.form['disponibilidad'],
        "id_invitado": request.form['id_invitado'],
    }
    invitados.update(data)
    return redirect(f"/show/{id_invitado}")

## ________________________________________##

@app.route('/delete/<int:id_invitado>')
def delete(id_invitado):
    data = {
        'id': id_invitado,
    }
    invitados.destroy(data)
    return redirect('/invitados')