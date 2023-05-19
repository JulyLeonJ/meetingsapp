from controller import invitados
from config.mysqlconnection import connectToMySQL

class Invitados:
    def __init__(self,data): ##metodo de instancia
        
        self.id_invitado = data['id_invitado']
        self.disponibilidad = data['disponibilidad']
        
## ___________________________________________________##
    @classmethod
    def save(cls,data): ##metodo de clase 
        query = "INSERT INTO invitados (id_invitado,disponibilidad) VALUES (%(id_invitado)s,%(disponibilidad)s))"
        return connectToMySQL('invitados_schema').query_db(query,data)

## ___________________________________________________##

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM invitados WHERE id_invitado = %(id_invitado)s;"
        invitados_from_db = connectToMySQL('invitados_schema').query_db(query,data)

        return cls(invitados_from_db[0])

        # Lógica para obtener un usuario de la base de datos por su ID
    
## ___________________________________________________##
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM invitados;"
        invitados_from_db =  connectToMySQL('invitados_schema').query_db(query)
        invitados =[]
        for b in invitados_from_db:
          invitados.append(cls(b))
        return invitados
    
## ___________________________________________________##    
    
    @classmethod
    def update(cls,data):
        # Lógica para actualizar un usuario en la base de datos
        query = "UPDATE invitados SET disponibilidad=%(disponibilidad)s WHERE id_invitado = %(id_invitado)s;"
        return connectToMySQL('invitados_schema').query_db(query,data)


## ___________________________________________________##
   
    @classmethod
    def delete(cls,data):
        # Lógica para eliminar un usuario de la base de datos por su ID
        query = "DELETE FROM invitados WHERE id = %(id_invitado)s;"
        return connectToMySQL('invitados_schema').query_db(query,data)
    
## ___________________________________________________##

    