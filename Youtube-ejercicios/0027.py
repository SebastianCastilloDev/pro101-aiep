# generar 100  numeros aleatorios (entre 0 y 100) y determinar y listar cuales son impares

# 1,4,3,5,5,6,6,4,3,3,4,5
# [1,3,5,5,3,3,5]

import random
from os import system
system('clear')

lista = []

for i in range(100):
    numerorandom = random.randint(0, 100)
    # si numerorandom es impar
    if numerorandom % 2 != 0:
        lista += [numerorandom]
print(lista)
