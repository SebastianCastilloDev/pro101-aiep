# Python - Ejercicio 169: Uso de Parámetros Sólo Posicionales en Python 3.8.0

def funcion(a, b, /, c, d, *, e, f):
    return 0

# a no puede ser pasado como a=2, b tampoco


funcion(1, 2, 3, d=4, e=5, f=6)
