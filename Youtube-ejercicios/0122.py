# Python - Ejercicio 122: Gestión de una Excepción Tipo Aritmética

try:
    print(1/0)
except ZeroDivisionError as e:
    print('Error:', e)
