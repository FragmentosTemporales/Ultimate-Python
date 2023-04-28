# creamos una tupla llamada numeros

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# creamos una tupla con una lista de base

punto = tuple([1, 2])
print(punto)

# creamos una nueva tupla filtrando por index
menosNumeros = numeros[:4]
print(menosNumeros)

# desempaquetamos una tupla

primero, segundo, *otros = numeros
print(primero, segundo, otros)

# iteramos una tupla

for n in numeros:
    print(n)
    
# creamos una nueva lista con el método list a la tupla numeros

listaNumeros = list(numeros)
print(listaNumeros)