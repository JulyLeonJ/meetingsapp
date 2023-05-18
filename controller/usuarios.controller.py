from flask import render_template, redirect, request, session, session, flash
from model import usuarios

@app.route('/')
def index():
    return render_template("index.html",usuarios= usuarios.get_all())

@app.route('/create',methods=['GET'])
def create():
    data = {
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
            }
    usuarios.save(data)
    return redirect('/usuarios')

@app.route('/')
def usuarios():
    return render_template("results.html",all_users=usuarios.get_all())


@app.route('/show/<int:id_usuario>')
def detail_page(id_usuario):
    data = {
        'id': id_usuario
    }
    return render_template("details_page.html",usuarios=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')