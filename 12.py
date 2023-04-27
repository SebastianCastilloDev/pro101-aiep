"""Programa 12"""

# 12. Escribe un programa que lea tres números enteros y devuelva el mayor de los tres

numero1 = int(input('numero1: '))
numero2 = int(input('numero2: '))
numero3 = int(input('numero3: '))

if numero1 > numero2:
    mayor = numero1
else:
    mayor = numero2

if mayor < numero3:
    mayor = numero3

print('el numero mayor es: ', mayor)
