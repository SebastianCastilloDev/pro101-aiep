# Python - Ejercicio 120: Limitar la Visualización del Número de Caracteres de una Cadena

lenguaje = 'Python es tremendo'

n = 5

print(lenguaje[:n])
print(str('%.'+str(n)+'s') % lenguaje)

cadena = '1234567'
print(cadena[:n])
print(str('%.'+str(n)+'s') % cadena)
