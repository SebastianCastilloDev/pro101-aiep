# Ejercicio 25: crear un histograma a partir de una lista de enteros.

# Ejemplo dada una lista = [2,4,3]
# escribir
# **
# ****
# ***

from os import system
system("clear")


def histograma(lista):
    for i in range(len(lista)):
        print(str(lista[i]) + ': ' + 'x'*lista[i])


lista = [2, 4, 3, 4, 8]
histograma(lista)
