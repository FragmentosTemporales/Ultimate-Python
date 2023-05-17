class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __del__(self):
        print(f"Perro eliminado {self.nombre}")
    
    def __str__(self):
        return f"clase Perro: {self.nombre}"    
    
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
        
perro = Perro("Chocolo", 7)
del perro