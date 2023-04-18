# 16. Escribe un programa que solicite dos números enteros positivos y calcule su producto usando sólo sumas.

numero1 = int(input('Ingresa un numero positivo: '))
numero2 = int(input('Ingresa otro numero positivo: '))

i = 0
total = 0
while i < numero1:
    total = total + numero2
    i = i + 1

print('Resultado: ', total)