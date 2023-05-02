# Python - Ejercicio 135: Comprobar si un Elemento de Programa es Generador

from inspect import isgenerator


def generador_impares():
    numero = 1
    yield numero

    while True:
        numero += 2
        yield numero


impares = generador_impares()

print(isgenerator(impares))

print(next(impares))
print(next(impares))
print(next(impares))
print(next(impares))
