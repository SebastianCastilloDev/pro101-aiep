# # Ejercicio 12
# Escribir un programa que almacene las matrices
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[-1, 0], [0, 1], [1, 1]]

for i in m1:
    for j in i:
        print(j)
