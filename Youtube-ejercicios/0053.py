# Python - Ejercicio 53: Consultar las Variables de Entorno del Sistema

import os

# conocer la ruta del usuario actual
print(os.environ['HOME'])
print('*'*50)
print(os.environ['PATH'])
print('*'*50)
print(os.environ)  # devuelve un diccionario con las variables de entorno
