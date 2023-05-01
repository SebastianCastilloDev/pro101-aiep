# Python - Ejercicio 102: Mostrar el Contenido de un Directorio por Medio de subprocess

import subprocess

resultado = subprocess.check_output('ls', shell=True, universal_newlines=True)

print(resultado)
print(type(resultado))
print(len(resultado))
