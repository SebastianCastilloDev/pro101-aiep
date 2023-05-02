# Python - Ejercicio 157: Contar las Ocurrencias de las Letras en un Archivo de Texto Plano

import collections
import pprint

nombre_archivo = '0156.py'

with open(nombre_archivo, 'r') as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)

print(conteo_caracteres)
print(salida)
