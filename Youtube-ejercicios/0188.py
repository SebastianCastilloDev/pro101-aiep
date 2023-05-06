# Python - Ejercicio 188: Calcular la Moda de un Conjunto de Datos Numéricos o Nominales

from statistics import mode

numeros = [2, 3, 3, 33, 2, 22, 2, 2, 33, 2, 2, 32, 23,
           23, 32, 223, 23, 0, 32, 2, 3, 32, 2, 22, 2, 2, 22, 3]

moda = mode(numeros)
print(moda)
