try:
    n1 =int(input("Ingresa primer número: "))
except ValueError as e:
    print("Ingrese un valor que corresponda" )
except NameError as e:
    print("Ocurrió un error")  
else:
    print("No ocurrió ningún error")
    
finally:
    print("se ejecuta siempre")