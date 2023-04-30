# calcular la suma de tres numeros, incluir una condicion de igualdad


def sumacion(a, b, c):
    suma = 0
    if a == b and a == c:
        suma *= 3
    else:
        suma = a+b+c
    return suma


print(sumacion(3, 3, 3))
