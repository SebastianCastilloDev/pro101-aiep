# mostrar la fecha de un evento almacenada en una tupla

import datetime

fecha_evento = (2023, 9, 14)

print('Fecha: %i/%i/%i ' % fecha_evento)

anio, mes, dia = fecha_evento
print('Fecha: {}/{}/{} '.format(anio, mes, dia))
