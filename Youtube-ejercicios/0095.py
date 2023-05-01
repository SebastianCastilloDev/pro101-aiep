# Python - Ejercicio 95: Validar si una Cadena de Caracteres Representa un Número

def es_numerico(t):
    try:
        float(t)
        return True
    except (TypeError, ValueError):
        return False


print(es_numerico('3.4223'))
print(es_numerico('3.4223a'))
