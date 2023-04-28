saludo = 25

def saludar():
    global saludo
    saludo= "Hola mundo"
    
#   Global nos deja utilizar una variable global y modificarla en la función

#   resultado 1 suma 3 al valor de saludo 

resultado1 = saludo + 3
print(resultado1)

#   acá se ejecuta el cambio del valor de saludo por un string

saludar()

#   le pedimos concatenar un string con un int, arrojando el error por consola

resultado2 = saludo + 3
print(resultado2)