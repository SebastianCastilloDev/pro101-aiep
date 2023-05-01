from os import listdir
from os import getcwd
from os.path import isfile, join

ruta = getcwd()

# Crear un nuevo archivo README.md que contiene los titulos de los ejercicios. Si el archivo existe, lo borra y crea un nuevo, con las correcciones que se hayan hecho en los archivos.py

readme = open('README.md', 'w')
texto_readme = """
# Resumen de ejercicios 

Este archivo README, ha sido generado con el archivo "resumen_de_ejercicios.py"
Su función es listar los enunciados de los ejercicios
Adicionalmente va acompañado de dos archivos más:
1. "creadordearchivos.py": Genera archivos con el formato '0'*n.py . Si el archivo ya existe, entonces no lo reemplaza.
2. "modificadordenombresdearchivo.py": Modifica los nombres de archivos con aspecto numerico y les da un formato tipo '0'*n.py y lo renombra.
Dentro de estos archivos se encuentra la variable 'digitos', la cual define cuantos ceros a la izquierda contendrá el nuevo nombre del archivo

Si un archivo no contiene nada en la primera linea, no lo agrega a este README.

Por tanto se debe colocar la descripcion del ejercicio en la primera linea de cada archivo.

## Lista de ejercicios:


"""


def listar_directorio(ruta):
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]
    return archivos


lista_archivos = listar_directorio(ruta)
lista_archivos.sort()


# Solo vamos a tomar la primera linea de los archivos que tengan formato '0'*n.py
for archivo in lista_archivos:
    if archivo.split('.')[0].isdigit() and archivo.split('.')[-1] == 'py':
        archivo_leido = open(archivo, 'r')

        contenido_primera_linea = archivo_leido.readline()
        if contenido_primera_linea:
            texto = "* [" + archivo + "]" + "(" + archivo + ")" + \
                ': ' + contenido_primera_linea
            texto_readme = texto_readme + texto
        archivo_leido.close()

# print(lista_archivos)


# Escribir y cerrar el archivo readme
readme.write(texto_readme)

readme.close()
