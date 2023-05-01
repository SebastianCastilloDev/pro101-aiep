# Python - Ejercicio 106: Separar la Ruta de la Extensión de Archivo

import os.path


rutas = [
    '/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios/0001.py',
    '/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios',
    '',
    'lenguajes.txt',
    'code',
    '/'
]

for ruta in rutas:
    print(ruta, os.path.splitext(ruta))
