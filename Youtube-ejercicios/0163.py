# Python - Ejercicio 163: Generar Combinaciones por Medio del Módulo itertools

from itertools import combinations


numeros = [1, 2, 3, 4]

for c in combinations(numeros, 3):
    print(c)
print()
[print(c) for c in combinations(numeros, 2)]
[print(c) for c in combinations(numeros, 4)]
[print(c) for c in combinations(numeros, 7)]
