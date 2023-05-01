# Python - Ejercicio 102: Mostrar el Contenido de un Directorio por Medio de subprocess

import os

ruta = '/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios/0001.py'

nombre_archivo = os.path.basename(ruta)

print(nombre_archivo)
