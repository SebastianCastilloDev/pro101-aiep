# Este programa modifica los nombres de archivos numericos a un formato '0'*n

from os import listdir
from os import rename
from os import getcwd
from os.path import isfile, join

ruta = getcwd()

digitos = 4
# Listar los archivos


def listar_directorio(ruta):
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]
    return archivos


lista_archivos = listar_directorio(ruta)

# verificar si el nombre del archivo contiene solo digitos, si es asi se crea un nuevo nombre con ceros a la izquierda
for archivo in lista_archivos:
    nombre = archivo.split('.')[0]
    if nombre.isdigit():
        nuevo_nombre = str(nombre).rjust(digitos, '0') + \
            '.'+archivo.split('.')[-1]
        # print(archivo, nuevo_nombre, sep='->')

        # modificar el nombre del archivos
        rename(archivo, nuevo_nombre)
