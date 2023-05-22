from controller import reuniones_controller
from config.mysqlconnection import connectToMySQL
import consumegoogle

class Reuniones:
    def __init__(self,data): ##metodo de instancia
        
        self.id_reunion = data['id_reunion']
        self.titulo = data['titulo']
        self.duracion = data['duracion']
        self.lugar = data['lugar']
        self.organizador = data['organizador']
        self.hora = data['hora']
        self.disponibilidad = data['disponibilidad']
        self.id_invitado = data['id_invitado']
        
## ___________________________________________________##
    @classmethod
    def save(cls,data): ##metodo de clase 
        query = "INSERT INTO reuniones (titulo,duracion,lugar,organizador,horainicio,horafinal,disponibilidad,id_invitado) VALUES (%(titulo)s,%(duracion)s,%(lugar)s,%(organizador)s,%(horainicio)s,%(horafinal)s,%(disponibilidad)s,%(id_invitado)s))"
        consumegoogle.create_event(titulo,horainicio,horafinal):
        return connectToMySQL('bd_meetings').query_db(query,data)

## ___________________________________________________##

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM reuniones WHERE id_reunion = %(id_reunion)s;"
        reuniones_from_db = connectToMySQL('bd_meetings').query_db(query,data)

        return cls(reuniones_from_db[0])

        # Lógica para obtener un usuario de la base de datos por su ID
    
## ___________________________________________________##
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reuniones;"
        reuniones_from_db =  connectToMySQL('bd_meetings').query_db(query)
        reuniones =[]
        for b in reuniones_from_db:
          reuniones.append(reuniones_from_db)
        return reuniones
    
## ___________________________________________________##    
    
    @classmethod
    def update(cls,data):
        # Lógica para actualizar un usuario en la base de datos
        query = "UPDATE reuniones SET titulo=%(titulo)s, duracion=%(duracion)s, lugar=%(lugar)s, organizador=%(organizador)s,hora=%(hora)s,disponibilidad=%(disponibilidad)s,id_invitado=%(id_invitado)s WHERE id_reunion = %(id_reunion)s;"
        return connectToMySQL('bd_meetings').query_db(query,data)


## ___________________________________________________##
   
    @classmethod
    def delete(cls,data):
        # Lógica para eliminar un usuario de la base de datos por su ID
        query = "DELETE FROM reuniones WHERE id = %(id_reunion)s;"
        return connectToMySQL('bd_meetings').query_db(query,data)
    
## ___________________________________________________##

    