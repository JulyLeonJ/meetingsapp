from controller import usuarios
from config.mysqlconnection import connectToMySQL
class Usuarios:
    def __init__(self,data): ##metodo de instancia
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.password = data['password']
        self.correo = data['correo']
        self.usuarios[]

## ___________________________________________________##
    @classmethod
    def save(cls,data): ##metodo de clase 
        query = "INSERT INTO usuarios (nombre,apellido,password,corrreo) VALUES (%(nombre)s,%(apellido)s,%(password)s,%(correo)s))"
        return connectToMySQL('usuarios_schema').query_db(query,data)

## ___________________________________________________##

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM usuarios id_usuario = %(id_usuario)s;"
        usuarios_from_db = connectToMySQL('usuarios_schema').query_db(query,data)

        return cls(usuarios_from_db[0])

        # Lógica para obtener un usuario de la base de datos por su ID
    
## ___________________________________________________##
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_from_db =  connectToMySQL('usuarios_schema').query_db(query)
        usuarios =[]
        for b in usuarios_from_db:
          usuarios.append(cls(b))
        return usuarios
    
## ___________________________________________________##    
    
    @classmethod
    def update(cls,data):
        # Lógica para actualizar un usuario en la base de datos
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, password=%(password)s, correo=%(correo)s WHERE id = %(id_usuario)s;"
        return connectToMySQL('usuarios_schema').query_db(query,data)


## ___________________________________________________##
   
    @classmethod
    def delete(cls,data):
        # Lógica para eliminar un usuario de la base de datos por su ID
        query = "DELETE FROM usuarios WHERE id = %(id_usuario)s;"
        return connectToMySQL('usuarios_schema').query_db(query,data)
    
## ___________________________________________________##

    @classmethod
    def get_users_with_meetings(cls,data):
        # obtener usuarios que tienen programadas reuniones  
        query = "SELECT * FROM usuarios LEFT JOIN reuniones ON reuniones.organizador = id_usuario  WHERE organizador = %(id_usuario)s;"
        results = connectToMySQL('usuarios').query_db(query,data)
        usuarios = cls(results[0])
        for row_from_db in results:
            # Now we parse the topping data to make instances of toppings and add them into our list.
            reuniones_data = {
                'id': row_from_db['reuniones.id'],
                'topping_name': row_from_db['topping_name'],
                'created_at': row_from_db['toppings.created_at'],
                'updated_at': row_from_db['toppings.updated_at']
            }
            usuarios.reuniones.append(reuniones.Reuniones(reuniones_data))
        return usuarios