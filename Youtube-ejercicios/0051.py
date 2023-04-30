# Python - Ejercicio 51: Crear una Tupla Nombrada para Representar un Punto en el Plano

# class Punto:
#     def __init__(self,x,y):
#         self.x
#         self.y

from collections import namedtuple

Punto = namedtuple('Punto', ['x', 'y'])

punto1 = Punto(2, 3)
punto1 = Punto(2, -3)
