# convertir una cadena de caracteres a entero y a real

from os import system
system("clear")

cadena = '32.32345'

# real = float(cadena)
# print('real', real)ss

numeroseparado = cadena.split('.')
print(int(numeroseparado[0]))
