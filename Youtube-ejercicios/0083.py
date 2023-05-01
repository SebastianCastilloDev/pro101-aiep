# Python - Ejercicio 83: Comprobar si Todos los Elementos de una Lista Cumplen una Condición

# condicion numero > valor

numeros = [7, 3, 4, 2, 2, 11]

print(all(x > 1 for x in numeros))
print(all(x > 5 for x in numeros))
