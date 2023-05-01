# Python - Ejercicio 110: Obtener los Números Divisibles por 7 usando una Función Anónima

numeros = [3, 14, 29, 42, 70, 2, 7, 8, 9, 13]


def divisible(x): return x % 7 == 0


numeros_div_7 = filter(divisible, numeros)
numeros_div_7 = list(numeros_div_7)
print(numeros_div_7)
