# Python - Ejercicio 119: Formatear la Salida de un Número de Punto Flotante (float)

real = 1.41421356

print('valor de la variable `real`:%f' % real)
print('valor de la variable `real`:%.2f' % real)
print('valor de la variable `real`:%.7f' % real)  # ojo redondea

real = 1.00

print('valor de la variable `real`:%f' % real)
print('valor de la variable `real`:%.2f' % real)
print('valor de la variable `real`:%.7f' % real)
print('valor de la variable `real`:%.13f' % real)
