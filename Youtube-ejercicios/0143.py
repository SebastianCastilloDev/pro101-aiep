# Python - Ejercicio 143: Detectar el Modo del Sistema Operativo (32 ó 64 bits)

import struct
modo_so = struct.calcsize('P')*8

print(modo_so)
