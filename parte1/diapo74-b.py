# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo.

def hipotenusa(a, b):

    return int((a**2+b**2)**0.5)


cateto1 = int(input('Cateto1'))
cateto2 = int(input('Cateto2'))

print(hipotenusa(cateto1, cateto2))
