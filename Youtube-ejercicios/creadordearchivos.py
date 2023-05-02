# Este programa crea nuevos archivos python con el formato '0'*n.py. Pero si un archivo existe con el mismo nombre, no lo sobre escribe


from os import listdir
from os import getcwd
from os.path import isfile, join

digitos = 4
desde = 151
hasta = 200

# Listar los archivos del directorio
ruta = getcwd()


def listar_directorio(ruta):
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]
    return archivos


lista_archivos = listar_directorio(ruta)


for i in range(desde, hasta+1):
    # generar nombre de archivo
    nombre_archivo = str(i).rjust(digitos, '0')+'.py'

    # Si el archivo existe, no lo sobre escribe
    if nombre_archivo in lista_archivos:
        print(nombre_archivo, 'ya existe')
    else:
        nuevo_archivo = open(nombre_archivo, 'w')
        print(nombre_archivo, 'ha sido creado')
        nuevo_archivo.close()

# print(call(['ping', 'google.com']))
