# Python - Ejercicio 76: Obtener los Argumentos de Línea de Comandos

import sys

nombre_script = sys.argv[0]
cantidad_argumentos = len(sys.argv)
argumentos = str(sys.argv)

print(nombre_script)
print(cantidad_argumentos)
print(argumentos)
