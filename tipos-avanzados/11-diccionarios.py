punto = {
    "x": 25,
    "y": 50
}
print(punto)
print(punto["x"])
print(punto["y"])
punto["z"] = 45

if "lala" in punto:
    print("encontré lala", punto["lala"])
    
print(punto.get("x"))
print(punto.get("lala", 1991))

del punto["x"]
del (punto ["y"])
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)
    
usuarios = [
    {
        "id": 1,
        "nombre": "Cristian",
        "edad": 31
    },
    {
        "id": 2,
        "nombre": "Dante",
        "edad": 4
    },
    {
        "id": 3,
        "nombre": "Javiera",
        "edad": 25
    },
]

for usuario in usuarios:
    print(usuario["nombre"])

print(usuarios)