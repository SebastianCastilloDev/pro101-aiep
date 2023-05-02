# Python - Ejercicio 126: Encontrar el Módulo al que Pertenece un Elemento de Programa

from inspect import getmodule

from math import sin

print(getmodule(sin))
print(type(getmodule(sin)))
print(dir(type(getmodule(sin))))
