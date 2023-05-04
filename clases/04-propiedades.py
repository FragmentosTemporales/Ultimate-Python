class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.name = nombre
        self.edad = edad
        
    def habla(self):
        print(f"{self.name} dice: Guau!")

Perro.patas = 3
mi_perro = Perro("Chocolo", 2)
mi_perro.patas = 5
mi_perro2 = Perro("Cachupín", 1)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
