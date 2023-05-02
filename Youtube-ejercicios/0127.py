# Python - Ejercicio 127: Comprobar si Elemento de Programa Dado es una Clase

from inspect import isclass
from collections import Counter
from math import cos

print(isclass(Counter))
print(isclass(cos))


class Clase:
    pass


def funcion():
    pass


print(isclass(Clase))
print(isclass(funcion))
