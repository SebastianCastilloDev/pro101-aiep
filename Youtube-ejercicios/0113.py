# Python - Ejercicio 113: Validar si un Número Ingresado por el Usuario es Válido


def es_numero(cadena):
    try:
        float(cadena)
        return True
    except Exception as e:
        print(e)
        return False


numero = input('ingrese un numero: ')

if es_numero(numero):
    print('numero valido')
else:
    print('no es numero')
