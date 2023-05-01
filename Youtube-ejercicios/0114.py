# Python - Ejercicio 114: Usar la Función filter para Obtener los Números Positivos de una Lista

numeros = [-2, 4, 5, -5, 5, 9, -10]
positivos = filter(lambda x: x >= 0, numeros)
print(list(positivos))
