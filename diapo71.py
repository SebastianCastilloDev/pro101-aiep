# Dado el programa que pide al usuario su nombre y lo saluda.
# Modifique el programa para que diga:
# Buenos días <nombre_usuario>
# Buenas tardes <nombre_usuario>
# Buenas noches <nombre_usuario>


import datetime

#https://www.codigopiton.com/como-obtener-la-hora-actual-en-python/
hora_actual = datetime.datetime.now().hour

nombre = input('Ingrese nombre: ')

if hora_actual > 8 and hora_actual <= 12:
    print('Buenos días ', nombre)
if hora_actual > 12 and hora_actual <= 20:
    print('Buenas tardes ', nombre)
if hora_actual > 20 and hora_actual <= 24:
    print('Buenas noches ', nombre)

if hora_actual > 0 and hora_actual <= 8:
    print('ANDA COSTATE!!')