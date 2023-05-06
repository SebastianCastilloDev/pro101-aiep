# Python - Ejercicio 196: Encontrar Una o Más Combinaciones de Tamaño n que Suman un Valor Dado

from itertools import combinations

while True:
    print('ingrese el tamaño de las combinaciones y el valor de la suma:', end='')
    n, suma = map(int, input().split())

    if n == 0 and suma == 0:
        break

    combinaciones = list(combinations(range(10), n))

    for c in combinaciones:
        if sum(c) == suma:
            print(c, suma)
