# Python - Ejercicio 111: Seleccionar Archivos de un Tipo Específico

import glob
import os

ruta = '/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios'

extension = '*.md'

lista_archivos = glob.glob(ruta + os.path.sep + extension)

print(lista_archivos)
