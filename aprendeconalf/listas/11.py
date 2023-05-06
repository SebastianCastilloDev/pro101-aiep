# Ejercicio 11 Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

x = [1, 2, 3]
y = [-1, 0, 2]

# determinando la longitud del vector
longitud = 0
for i in x:
    longitud += 1

producto = 0
for i in range(longitud):
    producto += x[i]*y[i]

print(producto)
