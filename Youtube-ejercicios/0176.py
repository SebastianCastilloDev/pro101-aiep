# Python - Ejercicio 176: Contar la Cantidad de Divisores de un Número Entero Positivo

def contar_divisores(n):
    contador_divisores = 0

    for i in range(1, n+1):
        if n % i == 0:
            contador_divisores += 1

    return contador_divisores


def divisores(n):
    return len([i for i in range(1, n+1) if n % i == 0])


print(contar_divisores(8))
print(divisores(8))
