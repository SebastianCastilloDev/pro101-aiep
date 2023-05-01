# Python - Ejercicio 63: Comprobar si el Nombre de un Archivo Corresponde con una Ruta Absoluta

from os import path

nombre_archivo_1 = '0061.py'
nombre_archivo_2 = r'/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/0061.py'

print(path.isabs(nombre_archivo_1))
print(path.isabs(nombre_archivo_2))
print(__file__)
print(path.isabs(__file__))
