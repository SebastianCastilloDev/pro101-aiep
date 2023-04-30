# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros = []

for i in range(6):
    numero = int(input('ingrese un numero para la loteria'))
    numeros += [numero]
numeros.sort()
print('los numero ganadores son: ' + str(numeros))
