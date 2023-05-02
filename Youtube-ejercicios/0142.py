# Python - Ejercicio 142: Obtener los Datos Básicos de la Plataforma Operacional

import os
import platform

print('Nombre: ', os.name)
print('sistema operativo: ', platform.system())
print('Version: ', platform.release())
