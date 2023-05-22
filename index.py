from flask import Flask, render_template,redirect, url_for,request
from config.mysqlconnection import connectToMySQL
##from vidstream import *
from controller.invitados_controller import Invitados
from controller.reuniones_controller import Reuniones
from controller.usuarios_controller import Usuarios
import consumegoogle
from app import app
import tkinter as tk
import socket
import threading


                                                    
@app.route('/')#creando rutas
def index():
    return render_template('home.html')

if __name__ == '__main__':
    
    app.run(debug=True)
                                                    #corriendo app 
local_ip_address = socket.gethostbyname(socket.gethostname())

