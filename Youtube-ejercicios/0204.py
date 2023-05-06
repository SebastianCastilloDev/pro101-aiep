# Python - Ejercicio 204: Sumar Todos los Números que Aparecen en una Cadena de Caracteres

import re

cadena = 'H0l4 3 MundO 4'

# utilizaremos expresiones regulares


def sumar_digitos_cadena(cadena):
    patron = r'[0-9]{1,7}'
    resultado = r'[0-9]{1-7}'
    numeros = re.findall(patron, cadena)
    numeros = map(int, numeros)
    return sum(numeros)


print(sumar_digitos_cadena(cadena))
