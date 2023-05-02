# Factorial

from functools import reduce


def calcula_factorial(n):

    if n == 0:
        factorial = 0
    elif n == 1:
        factorial = 1
    else:
        numeros = range(1, n+1)
        factorial = reduce(lambda x, y: x*y, numeros)

    return factorial


print(calcula_factorial(0))
print(calcula_factorial(1))
print(calcula_factorial(2))
print(calcula_factorial(3))
print(calcula_factorial(4))
print(calcula_factorial(5))
