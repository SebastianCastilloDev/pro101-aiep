# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = []
for i in range(10):
    numeros.append(i+1)

cadena = ''
# invertir los numeros
for i in range(1, len(numeros)+1):
    if i < len(numeros):
        cadena += str(numeros[-i]) + ','
    else:
        cadena += str(numeros[-i])
print(cadena)
