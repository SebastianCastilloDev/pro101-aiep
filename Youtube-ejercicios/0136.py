# Python - Ejercicio 136: Excluir Directorios de un Listado de Archivos y Carpetas

import os
ruta = '/Users/sebastiancastillo/Documents/aiep/pro101'

archivos = [f for f in os.listdir(
    ruta) if os.path.isfile(os.path.join(ruta, f))]
