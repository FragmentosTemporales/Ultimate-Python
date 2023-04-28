def no_space(texto):
#Eliminar espacios en el texto
    resultado = ""
    for letra in texto:
        if letra != " ":
            resultado += letra        
    return resultado

def reverse(texto):
    texto_invertido = ""
    for letra in texto:
        texto_invertido = letra + texto_invertido
    return texto_invertido

def es_palindromo(texto):
    texto = no_space(texto)
    texto_invertido = reverse(texto)
    if texto.lower() == texto_invertido.lower():
        print("Son palíndromos")
    else:
        print("No son palíndromos")
 
nombre = input("Ingresa el texto: ")        
es_palindromo(nombre)
    