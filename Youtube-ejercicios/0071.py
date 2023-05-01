# Python - Ejercicio 71: Calcular el Tamaño de un Archivo en bytes

import os

archivo = r'/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios/0019.py'


def calcular_tamano(archivo):
    try:
        return (os.path.getsize(archivo))
    except:
        return None


print(calcular_tamano(archivo))
