# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo.

cateto1 = float(input('Cateto 1: '))
cateto2 = float(input('Cateto 2: '))

hipotenusa = (cateto1**2+cateto2**2)**0.5

print('Hipotenusa: ', hipotenusa)