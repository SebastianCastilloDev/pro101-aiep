# Python - Ejercicio 165: Calcular la Suma de Dos Números usando operadores de bits


# usaremos operadores nivel bit
# https://ellibrodepython.com/operadores-bitwise

def suma(a, b):
    while b != 0:
        temp = a & b
        a = a ^ b
        b = temp << 1
    return a


print(suma(3, 5))
