# Python - Ejercicio 129: Rellenar una Cadena de Caracteres con un Carácter Específico

# Python => ***Python***

cadena = 'Python'

caracter = '*'
n = 3

print(cadena.rjust(len(cadena)+n, caracter).ljust(len(cadena)+2*n, caracter))
