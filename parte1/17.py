# 17. Escribir un programa que calcule la suma de los pares que hay entre dos números dados como entrada.

numero1 = int(input('Ingrese numero1: '))
numero2 = int(input('Ingrese numero2: '))

i = numero1
total = 0
while i <= numero2:
    if i%2 == 0:
        total = total + i
    i = i + 1

print('El total de la suma de los pares entre ', numero1, ' y ', numero2, ' es ', total)