# Python - Ejercicio 154: Obtener las Tripletas de Números Diferentes Cuya Suma es Cero

from itertools import permutations


def obtener_tripletas(numeros):

    perms = permutations(numeros, 3)

    tripletas = []
    for perm in list(perms):
        if sum(perm) == 0:
            tripletas.append(perm)
    return tripletas


lista = [0, 3, 2, -2, 1, -1, 3, 4, 5, 6, 3, 3, 2, 2, 2, 23, 3, 3, 3]
print(obtener_tripletas(lista))
