class Perro:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.edad = edad
        
    def habla(self):
        print(f"{self.name} dice: Guau!")

mi_perro = Perro("Chocolo", 2)
print(mi_perro.name)
mi_perro.habla()