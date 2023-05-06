# Python - Ejercicio 208: Calcular el Área de un Polígono Regular Dados el Número de Lados

from math import tan, pi

# n=numero de lados
# lado=longitud del lado


def area_poligono(n, lado):
    return n*lado**2/(4*tan(pi/n))


print(area_poligono(5, 12))
