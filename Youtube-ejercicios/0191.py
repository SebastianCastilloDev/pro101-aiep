# Python - Ejercicio 191: Obtener Múltiples Modas desde un Conjunto de Datos Numéricos o Nominales

from statistics import multimode

numeros = [3, 2, 7, 4, 34, 4, 3, 3, 3, 3, 44, 4, 4, 4, 4, 44, 3, 3, 33, 3,
           3, 2, 2, 2, 2, 3, 3, 3, 34, 4, 4, 5, 5, 5, 4, 4, 4, 4, 44, 5, 5, 5, 55, 2, 1]

print(multimode(numeros))
