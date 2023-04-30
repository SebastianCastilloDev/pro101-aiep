# ejercicio 14: calcular la diferencia ej dias de dos fechas dadas

from datetime import date

hoy = date(2023, 3, 1)
fecha = date(2023, 2, 13)

delta = fecha - hoy

print(delta)
print(delta.days)
