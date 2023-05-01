# Python - Ejercicio 107: Obtener las Propiedades Básicas de un Archivo
import os
import time

archivo = '/Users/sebastiancastillo/Documents/aiep/pro101/ejercicios-parte-1/Youtube-ejercicios/0001.py'

print('f mod: ', time.ctime(os.path.getmtime(archivo)))
print('f cre: ', time.ctime(os.path.getctime(archivo)))
print('f acceso: ', time.ctime(os.path.getatime(archivo)))
print('tamaño: ', os.path.getsize(archivo))
print('ruta absoluta: ', os.path.abspath(archivo))
print('directorio: ', os.path.dirname(archivo))
print('lista de rutas comunes: ', [os.path.commonprefix(archivo)])
print('Existe?: ', os.path.exists(archivo))
print('Es ruta absoluta?: ', os.path.isabs(archivo))
print('Es directorio?: ', os.path.isdir(archivo))
print('Es un archivo?: ', os.path.isfile(archivo))
print('Es un enlace?: ', os.path.islink(archivo))
print('Es un mount point?: ', os.path.ismount(archivo))
print('Existe la ruta?: ', os.path.lexists(archivo))
print('caracteres normalizados: ', os.path.normcase(archivo))
print('ruta normalizada', os.path.normpath(archivo))
print('ruta real: ', os.path.realpath(archivo))
print('ruta relativa: ', os.path.relpath(archivo))
print('archivo == archivo?: ', os.path.samefile(archivo, archivo))
print('(unidad(windows), ruta): ', os.path.splitdrive(archivo))
print('ruta+nombre, extension: ', os.path.splitext(archivo))
