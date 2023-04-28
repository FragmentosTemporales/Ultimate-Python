# numeros = [2, 4, 1, 14, 21, 7]
# numeros.sort()
# print(numeros)
# numeros2 = sorted(numeros, reverse= True)
# numeros.sort(reverse=True)
# print(numeros2) */

usuarios = [
    ["Cristian", 4],
    ["Dante", 1],
    ["Javiera", 5]
]
# def ordena(elemento):
#     return elemento[1]
# usuarios.sort(key=ordena, reverse=True)
# print(usuarios)
# usuarios.sort(key=ordena)
# print(usuarios)

usuarios.sort(key=lambda el: el[1])
print(usuarios)