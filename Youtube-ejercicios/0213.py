# Python - Ejercicio 213: Crear una Función para Computar la Longitud de un Texto sin Usar len

cadena = 'Sebastian Castillo'


def long_texto(cadena):
    longitug = 0
    for char in cadena:
        longitug += 1
    return longitug


print(long_texto(cadena))
