# Python - Ejercicio 166: Validar la Prioridad de los Operadores Suma, Resta, Producto y División

__prioridad__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}


def mayor_prioridad(operador_1, operador_2):
    return __prioridad__[operador_1] >= __prioridad__[operador_2]


print(mayor_prioridad('+', '*'))
