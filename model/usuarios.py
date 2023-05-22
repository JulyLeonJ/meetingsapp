from controller import usuarios_controller
from config.mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self,data): ##metodo de instancia
        self.id = data['id_usuario']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.password = data['password']
        self.correo = data['correo']
        
## ___________________________________________________##

    @classmethod
    def save(cls,data): ##metodo de clase 
        query = "INSERT INTO usuarios (id_usuario,nombre,apellido,password,corrreo) VALUES (%(id_usuario)%,%(nombre)%,%(apellido)%,%(password)%,%(correo)%))"
        return connectToMySQL('bd_meetings').query_db(query,data)

## ___________________________________________________##

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM usuarios id_usuario = %(id_usuario)s;"
        usuarios_from_db = connectToMySQL('bd_meetings').query_db(query,data)

        return cls(usuarios_from_db[0])

        # Lógica para obtener un usuario de la base de datos por su ID
    
## ___________________________________________________##
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_from_db =  connectToMySQL('bd_meetings').query_db(query)
        usuarios =[]
        for i in usuarios_from_db:
          usuarios.append(usuarios_from_db)
        return usuarios
    
## ___________________________________________________##    
    
    @classmethod
    def update(cls,data):
        # Lógica para actualizar un usuario en la base de datos
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, password=%(password)s, correo=%(correo)s WHERE id = %(id_usuario)s;"
        return connectToMySQL('bd_meetings').query_db(query,data)


## ___________________________________________________##
   
    @classmethod
    def delete(cls,data):
        # Lógica para eliminar un usuario de la base de datos por su ID
        query = "DELETE FROM usuarios WHERE id = %(id_usuario)s;"
        return connectToMySQL('bd_meetings').query_db(query,data)
    
## ___________________________________________________##

    