# Python - Ejercicio 64: Obtener la Fecha de Creación y Modificación de un Archivo

import os.path
import time

nombre_archivo = 'Youtube-ejercicios/0061.py'

fecha_creacion = time.ctime(os.path.getctime(nombre_archivo))
fecha_modificacion = time.ctime(os.path.getmtime(nombre_archivo))


print(fecha_creacion)
print(fecha_modificacion)
