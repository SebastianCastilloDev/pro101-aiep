# Python - Ejercicio 108: Consultar Propiedades de Archivos y Directorios

import os

rutas = ['0001.py', '/Users/sebastiancastillo',
         '/Users/sebastiancastillo/', os.path.dirname(__file__), __file__]

for ruta in rutas:
    print(ruta)
    print('existe: ', os.path.exists(ruta))
    print('abs: ', os.path.isabs(ruta))
    print('es archivo?: ', os.path.isfile(ruta))
    print('es carpeta?: ', os.path.isdir(ruta))
