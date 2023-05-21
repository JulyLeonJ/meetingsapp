from flask import Flask, render_template,redirect, url_for,request
from config.mysqlconnection import connectToMySQL
from vidstream import *
import tkinter as tk
import socket
import threading
import controller
                                                    #importando flask
app = Flask (__name__,template_folder='templates')
                                                    #creando app 
@app.route('/')#creando rutas
def index():
    return render_template('home.html')

if __name__ == '__main__':
    
    app.run(debug=True)
                                                    #corriendo app 
local_ip_address = socket.gethostbyname(socket.gethostname())



@app.route('/user/',methods=['GET']) ##que tipo de metodo estoy usando para consumir
def user():
    data = ["July"] ## data sera igual al nombre del metodo que estoy consumiendo del controlador
    return render_template('usuarios.html',listaUsuario=data[0]) ##voy a mostrar data mandandola a la vista del template

@app.route('/createUser/',methods=['POST']) ##que tipo de metodo estoy usando para consumir
def createUser():
    data = controller.invitados_controller.mostrar_Ejemplo()
    return render_template('usuarios.html',listaUsuario=data[0]) ##voy a mostrar data mandandola a la vista del template









