# Python - Ejercicio 70: Ordenar un Conjunto de Archivos por Fecha de Creación

# Este archivo debe ser ejecutado en la carpeta contenedora

import os
import glob

ruta = os.getcwd()
archivos = glob.glob(ruta + os.path.sep + '*.py')

archivos.sort(key=os.path.getctime)

print('\n'.join(archivos))
