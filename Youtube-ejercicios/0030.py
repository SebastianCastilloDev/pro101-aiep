# Calcular el MCD, maximo comun divisor de dos numeros.
from os import system
system('clear')

# 12 = 2,3,4,6,12
# 18= 2,3,6


# mostrando divisores de a


def mcd(x, y):

    mcd = 1

    if x % y == 0:
        return y

    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            mcd = i
            break
    return mcd


print(mcd(12, 18))
