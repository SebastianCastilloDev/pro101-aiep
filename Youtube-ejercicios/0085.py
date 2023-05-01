# Python - Ejercicio 85: Comprobar si una Ruta es un Directorio o un Archivo

import os


def comprueba_ruta(ruta):
    if os.path.isdir(ruta):
        return ('dir')
    elif os.path.isfile(ruta):
        return ('dir')
    else:
        return ('es un archivo especial')
