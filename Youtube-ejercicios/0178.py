# Python - Ejercicio 178: Computar la Suma del Valor Absoluto de Pares de Elementos de una Lista, los elementos deben estar ordenados de forma ascendente


from itertools import combinations


def suma_pares_diferentes(numeros):
    suma = 0
    for c in combinations(numeros, 2):
        suma += sum(c)
    return suma


lista = [1, 2, 3]
print(suma_pares_diferentes(lista))
