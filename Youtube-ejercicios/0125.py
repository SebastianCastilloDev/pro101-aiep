# Python - Ejercicio 125: Computar la Suma de los Conteos de los Duplicados de una Lista

from collections import Counter

numeros = [7, 5, 4, 4, 5, 5, 5, 43, 34, 3, 2, 0, 2,
           3, 3, 3, 4, 54, 5, 5, 5, 6, 6, 6, 6, 5, 5, 4, 3]

conteos = Counter(numeros)

print(conteos)

print(sum(conteos.values()))
