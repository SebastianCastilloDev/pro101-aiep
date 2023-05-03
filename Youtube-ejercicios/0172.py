# Python - Ejercicio 172: Explorar el Nuevo Soporte para Depuración por medio de f-strings

import datetime

nombre = 'Sebastian Castillo'

fecha = datetime.datetime.now()
print('nombre', nombre)
print('fecha', fecha)

# uso de f-strings:

print(f'{nombre=}')
print(f'{fecha=}')

fecha_nacimiento = datetime.date(1984, 8, 3)
hoy = datetime.date.today()
delta = hoy - fecha_nacimiento

print(f'{delta=}')
