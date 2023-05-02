# Haz un programa que lea un número binario y lo transforme a su equivalente decimal

binario = input('ingrese un numero binario: ')

contador = len(binario)-1
entero = 0
for numero in binario:
    entero += int(numero)*(2**contador)
    contador += -1

print(binario, "=", entero)
