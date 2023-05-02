# Python - Ejercicio 168: Uso Básico del Operador de Asignación Walrus de Python 3.8.0

# operador walrus    :=

cadena = 'Python'

if (l := len(cadena)) > 5:
    print(' la cadena tiene mas de 5 caracteres', 'tiene', l, 'caracteres')
