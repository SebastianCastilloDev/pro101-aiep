# Python - Ejercicio 35: Crear una Función Únicamente para Sumar Números Enteros

def sumar(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    else:
        raise TypeError('Los valores deben ser enteros')


try:

    print(sumar(2, 3))

    print(sumar(2, '3'))
except TypeError as e:
    print(e)
