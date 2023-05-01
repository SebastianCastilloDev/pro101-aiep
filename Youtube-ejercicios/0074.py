# Python - Ejercicio 74: Crear una Función para Calcular la Desviación Estándar

import statistics


def desviacion_estandar(valores):
    media = statistics.mean(valores)
    suma = 0
    for valor in valores:
        suma += (valor-media)**2
    desv = (suma/(len(valores)-1))**0.5
    return desv


print(desviacion_estandar([2, 3, 5, 4]))
