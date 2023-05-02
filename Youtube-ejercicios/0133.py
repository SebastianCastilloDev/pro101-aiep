# Python - Ejercicio 133: Calcular el Tiempo de Ejecución de una Función

from timeit import default_timer


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


inicio = default_timer()
fibonacci(20)
fin = default_timer()

print(fin-inicio)
