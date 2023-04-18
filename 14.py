# 14 Escribe un programa que lea diez números enteros y devuelva el mayor de todos ellos.

mayor = 0

i = 0
while i < 10:
    numero = int(input('Ingrese un numero entero: '))
    if numero > mayor:
        mayor = numero
    i = i + 1

print('El numero mayor es: ', mayor)