# Python - Ejercicio 92: Filtrar Números por medio de la Función filter

numeros = [i for i in range(10)]

# crear una expresion lambda


def filtro_impares(x): return x % 2 == 1


impares = filter(filtro_impares, numeros)

print(list(impares))
