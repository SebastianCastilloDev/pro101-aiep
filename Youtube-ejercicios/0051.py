# Python - Ejercicio 51: Crear una Tupla Nombrada para Representar un Punto en el Plano

# class Punto:
#     def __init__(self,x,y):
#         self.x
#         self.y

from collections import namedtuple
from math import sqrt

Punto = namedtuple('Punto', ['x', 'y'])

punto1 = Punto(2, 3)
punto2 = Punto(2, -3)

print(punto1)
print(punto2)


def calcular_distancia(punto_1, punto_2):
    return sqrt((punto_1.x-punto_2.x)**2 + (punto_1.y-punto_2.y)**2)


print(calcular_distancia(punto1, punto2))
