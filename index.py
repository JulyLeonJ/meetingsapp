from flask import Flask, render_template 
                                                    #importando flask
app = Flask (__name__,template_folder='templates')
                                                    #creando app 
@app.route('/')
                                                    #creando rutas
def Home():
    
    return render_template('templates/home.html')

if __name__ == '__main__':
    
    app.run(debug=True)
                                                    #corriendo app 
