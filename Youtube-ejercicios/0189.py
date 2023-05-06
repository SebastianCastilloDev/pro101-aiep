# Python - Ejercicio 189: Comprobar si Dos Números (o su Suma) Superan los 80 Dígitos


def comprobar_suma(n1, n2):
    return n1 >= 10**80 or n2 >= 10**80 or (n1+n2) >= 10**80
