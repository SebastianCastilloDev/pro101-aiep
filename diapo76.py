# Año bisiesto

anio = int(input('Ingrese el año: '))
# 1.- Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos.
# 2.- Sin embargo, los años divisibles entre 100 y entre 400 sí que son bisiestos.

if (anio % 4 == 0 and anio % 100 != 0) or (anio % (400) == 0):
    print('año bisiesto = ', anio)
else:
    print('El año no es bisiesto')
