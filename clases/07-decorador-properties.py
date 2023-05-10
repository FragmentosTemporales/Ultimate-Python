class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
        
    @property
    def nombre(self):
        print("Pasando por Getter")
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por Setter")
        if nombre.strip():
            self.__nombre = nombre
            
perro = Perro("Chocolo")
print(perro.nombre)
