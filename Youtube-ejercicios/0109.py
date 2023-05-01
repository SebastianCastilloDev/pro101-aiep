# Python - Ejercicio 109: Obtener el Valor de una Variable de Entorno

import os

variables_entorno = 'USER'
print(os.getenv(variables_entorno))
variables_entorno = 'COMMAND_MODE'
print(os.getenv(variables_entorno))
variables_entorno = '_'
print(os.getenv(variables_entorno))
