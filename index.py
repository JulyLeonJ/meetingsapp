from flask import Flask, render_template 
from vidstream import *
import tkinter as tk
import socket
import threading
import requests
                                                    #importando flask
app = Flask (__name__,template_folder='templates')
                                                    #creando app 
@app.route('/')
                                                    #creando rutas
def Home():
    
    return render_template('home.html')

if __name__ == '__main__':
    
    app.run(debug=True)
                                                    #corriendo app 
local_ip_address = socket.gethostbyname(socket.gethostname())