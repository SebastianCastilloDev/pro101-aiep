# Año bisiesto

def anio_bisiesto(anio):
    if(anio % 4 == 0 and anio % 100 != 0) or (anio % (4*100) == 0):
        print('El año ', anio, 'ES bisiesto')
    else:
        print('El año', anio, 'no es bisiesto' )

anio_bisiesto(1988)
anio_bisiesto(2011)
anio_bisiesto(1700)
anio_bisiesto(1500)
anio_bisiesto(2400)