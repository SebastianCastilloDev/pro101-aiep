# Ejercicio 55: convertir binario a entero

# 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0
from os import system
system("clear")

binario = '1001'

contador = len(binario)-1
entero = 0
for numero in binario:
    entero += int(numero)*(2**contador)
    contador += -1

print(entero)
