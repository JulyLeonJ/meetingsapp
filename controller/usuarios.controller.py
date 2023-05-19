from meetingsapp import app
from flask import render_template, redirect, request, session, session, flash
from model import Usuarios

@app.route('/')
def index():
    return render_template("home.html")

## ____________________________________________##



@app.route('/create',methods=['POST'])
def create():
    if request.method == 'POST'{
        
    
    data = {
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
            }
    Usuarios.save(data)
    }
    return redirect('/usuarios')

## ________________________________________##

@app.route('/usuarios')
def usuarios():
    return render_template("usuarios.html",all_usuarios=Usuarios.get_all())

    
    
    
    
 ##    
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = user.get_all()
    return render_template("listar_usuarios.html", usuarios = usuarios)

def listar_usuarios():
    # Lógica para obtener una lista de usuarios de la base de datos
    usuarios = User.obtener_todos()
    return render_template('listar_usuarios.html', usuarios=usuarios)


@app.route('/show/<int:id_usuario>')
def detail_page(id_usuario):
    data = {
        'id': id_usuario
    }
    return render_template("details_page.html",usuarios=usuario.get_one(data))

@app.route('/edit_page/<int:id_usuario>')
def edit_page(id_usuario):
    data = {
        'id': id_usuario
    }
    return render_template("edit_page.html", usuario = usuario.get_one(data))

@app.route('/update/<int:id_usuario>', methods=['POST'])
def update(id_usuario):
    data = {
        'id': id_usuario,
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "password": request.form['password'],
        "correo": request.form['correo'],
    }
    usuario.update(data)
    return redirect(f"/show/{id_usuario}")

@app.route('/delete/<int:id_usuario>')
def delete(id_usuario):
    data = {
        'id': id_usuario,
    }
    usuarios.destroy(data)
    return redirect('/usuarios')