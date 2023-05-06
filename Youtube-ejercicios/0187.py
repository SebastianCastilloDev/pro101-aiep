# Python - Ejercicio 187: Uso de las Funciones mean y fmean del Módulo statistics

from statistics import mean, fmean

numeros = [2, 3, 4, 5, 6, 7, 7, 8, 0]

promedio = mean(numeros)

numeros = [2.3, 3.3, 4.4, 5, 6, 7, 7, 8, 0]

promedio = fmean(numeros)  # float
