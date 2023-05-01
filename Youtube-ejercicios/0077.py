# Python - Ejercicio 77: Determinar el Orden de los Bytes en la Arquitectura de Ejecución Actual


import sys
if sys.byteorder == 'little':
    print('Plataforma little-endian')
else:
    print('Plataforma big-endian')
