# Python - Ejercicio 88: Formatear la Salida de una Cadena de Caracteres

x = 2
y = 3
suma = x + y
print('La suma de ' + str(x) + 'y' + str(y) + 'es igual a', str(suma))
print('La suma de', x, 'y', y, 'es igual a', suma)
print('La suma de %d y %d es igual a %d' % (x, y, suma))
print('La suma de {} y {} es igual a {}'.format(x, y, suma))
