# Calcular el area de un triangulo, dado sus lados.

from os import system
system('clear')


def areatriangulo(a, b):
    return a*b/2


a = float(input('Ingrese primer lado:'))
b = float(input('Ingrese segundo lado:'))

print(areatriangulo(a, b))
