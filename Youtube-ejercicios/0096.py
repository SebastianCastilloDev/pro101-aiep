# Python - Ejercicio 96: Imprimir el Estado de la Pila de Llamadas

import traceback


def funcion():
    xyz()


def xyz():
    traceback.print_stack()


funcion()
