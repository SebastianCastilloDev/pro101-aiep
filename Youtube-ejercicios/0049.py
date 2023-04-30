# Python - Ejercicio 49: Mostrar los Archivos de un Directorio Específico

from os import listdir
from os.path import isfile, join

ruta = '/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios'


def listar_directorio(ruta):
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]

    return archivos


print(listar_directorio(ruta))
