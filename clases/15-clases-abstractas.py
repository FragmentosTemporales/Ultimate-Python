from abc import ABC, abstractclassmethod

class Model(ABC):  
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    @property
    @abstractclassmethod
    def tabla(self):
        pass
    
    @abstractclassmethod        
    def guardar(self):
        pass
    
    @classmethod    
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")
        
class Usuario(Model):
    tabla = "Usuario"
    
    def guardar(self):
        print("guardando usuario")
    
usuario = Usuario()
usuario.guardar()