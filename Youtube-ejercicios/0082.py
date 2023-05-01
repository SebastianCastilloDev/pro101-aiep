# Python - Ejercicio 82: Calcular la Suma de los Elementos de un Objeto Iterable

import math

numeros = [13, 123, 123, 123, 123, 34, 24, 435, 35, 43, 345]

suma = 0

for numero in numeros:
    suma += numero

print('Suma de todos los numeros:', suma)

# otra forma

suma = sum(numeros)
print(suma)
