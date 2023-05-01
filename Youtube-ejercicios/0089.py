# Python - Ejercicio 89: Generar Números Aleatorios y Verificar que Todos sean Impares

from random import randint
n = 5


def generar_impares(n):
    impares = []

    while True:
        numeros = [randint(1, 10) for _ in range(n)]

        if all(x % 2 == 1 for x in numeros):
            impares = numeros
            break
    return impares


print(generar_impares(5))
