# Python - Ejercicio 91: Alternar el Contenido de Dos Variables

a = 2
b = 3

temp = a
a = b
b = temp

print(a, b)

# otra forma
a = 2
b = 3

a, b = b, a

print(a, b)
