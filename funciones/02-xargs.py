def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
    
    
def mostrar(*numeros):
    for numero in numeros:
        print(numero)

    
suma(2, 5)
mostrar(2, 5)
suma(2, 5, 7)
mostrar(2, 5, 7)
suma(2, 5, 9, 7)
mostrar(2, 5, 9, 7)