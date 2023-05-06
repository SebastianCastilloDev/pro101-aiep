# Ejercicio 10 Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# Solucion1:
lista = [50, 75, 46, 22, 80, 65, 8]
# print(min(lista))
# print(max(lista))

# Solucion2:
# lista.sort()
# print(lista[0])
# print(lista[-1])

# Solucion3:
menor = 200

for i in lista:
    if i < menor:
        menor = i
print(menor)


mayor = 0

for i in lista:
    if i > mayor:
        mayor = i
print(mayor)
