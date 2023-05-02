# Python - Ejercicio 148: Encontrar el Mínimo y el Máximo de una Lista sin Usar Funciones Existentes

lista = [3, 45, 5, 1, 2, 3, 43, 4, 3, 3, 2, 3, 4, 5]


def min_max(numeros):
    menor = numeros[0]
    mayor = numeros[0]

    for n in numeros:
        if n < menor:
            menor = n
        if n > mayor:
            mayor = n

    return menor, mayor


print(min_max(lista))
