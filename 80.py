# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

tiempo = True
acumulado = 0

while tiempo > 0:
    tiempo = int(input('Ingrese minutos: '))
    acumulado = acumulado + tiempo

horas = str(int(acumulado / 60))
minutos = acumulado % 60

# print(horas)
# print(minutos)

if minutos / 10 > 1:
    minutos = str(minutos)
else:
    minutos = '0'+ str(minutos)

texto = horas + ':' + minutos + ' horas'

print(texto)