# Año bisiesto

anio = int(input('Ingrese el año: '))

if(anio % 4 == 0 and anio % 100 != 0) or (anio % (4*100) == 0):
    print('año bisiesto = ', anio)
else:
    print('El año no es bisiesto' )
