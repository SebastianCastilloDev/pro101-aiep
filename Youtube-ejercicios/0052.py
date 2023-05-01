# Python - Ejercicio 52: Imprimir Cadenas de Caracteres en la Salida Estándar de Errores

import sys

# Esta salida es diferente


def errorprint(*args, **kwargs):
    print(*args, file=sys.stderr)


errorprint('Este es un mensaje de error')
