# Escribe un programa que lea diez números enteros y devuelva el mayor de todos ellos.

numeromayor = 0

for i in range(10):
    numero = int(input('Ingrese numero ' + str(i+1) + ': '))

    if numero > numeromayor:
        numeromayor = numero

print('el numero mayor es: ', numeromayor)
