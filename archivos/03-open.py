from io import open 

# escritura
# texto = "Hola mundo!"
# archivo = open("archivos/hola.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open("archivos/hola.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open("archivos/hola.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# with open("archivos/hola.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar
# archivo = open("archivos/hola.txt", "a+")
# archivo.write("Chao mundo :(")
# archivo.close

# lectura y escritura
with open("archivos/hola.txt", "r+") as archivo:
    texto = archivo.readlines()