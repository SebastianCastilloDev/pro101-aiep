# Python - Ejercicio 115: Calcular el Producto de los Elementos de una Lista sin Usar un Ciclo for

from functools import reduce

numeros = [-2, 4, 5, -5, 5, 9, -1]

producto = reduce(lambda x, y: x*y, numeros)

print(producto)

# factorial

numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x*y, numeros)

print(producto)
