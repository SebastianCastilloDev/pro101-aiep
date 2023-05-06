# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

numeros = [2, 3, 4, 5, 6, 67, 4, 34, 3, 3, 4, 4, 5, 65, 10, 77, 7, 56, 5, 5]


def longitud(numeros):
    longitud = 0
    for numero in numeros:
        longitud += 1
    return longitud


def suma(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


def media(numeros):
    return suma(numeros)/longitud(numeros)


def varianza(numeros):
    total = 0
    promedio = media(numeros)
    for numero in numeros:
        total += (numero-promedio)**2
    return total/longitud(numeros)


def desviacion_estandar(numeros):
    return varianza(numeros)**0.5


def calculadora_estadistica(numeros):
    return {"Media": media(numeros), "Varianza": varianza(numeros), "Desviacion Estandar": desviacion_estandar(numeros)}


print(calculadora_estadistica(numeros))
