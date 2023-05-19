from flask import Flask, render_template 
from vidstream import *
import tkinter as tk
import socket
from controller import reuniones_controller
from controller import invitados_controller
from controller import usuarios_controller
import threading
import requests
                                                    #importando flask
app = Flask (__name__,template_folder='templates')
                                                    #creando app 
@app.route('/')
                                                    #creando rutas
def index():
    
    return render_template('home.html')

if __name__ == '__main__':
    
    app.run(debug=True)
                                                    #corriendo app 
local_ip_address = socket.gethostbyname(socket.gethostname())

@app.route('/controller/usuarios_controller')
                                                    #creando rutas
def usuarios_controller():
    
    return render_template('home.html')

