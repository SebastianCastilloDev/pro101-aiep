# 7. La fecha de cualquier Domingo de Pascua se calcula de la siguiente forma:
# * Sea X el año para el que se quiere calcular la fecha. 
# * Sea A el resto de la división de X entre 19
# * Sea B el resto de la división de X entre 4
# * Sea C el resto de la división de X entre 7
# * Sea D el resto de la división de (19 * A + 24) entre 30
# * Sea E el resto de la división de (2 * B + 4 * C + 6 * D + 5) entre 7
# * La fecha para el Domingo de Pascua es el día (22 + D + E) de Marzo
# (obsérvese que puede dar una fecha en mes de Abril)
# Escribir un programa que pida como entrada un año y saque por pantalla la fecha del Domingo de Pascua para ese año.

anio = int(input('Ingrese el año: '))
a = anio % 19
b = anio % 4
c = anio % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7

dia = 22 + d + e

if (dia <= 31):
    print('El día de pascua es el ', dia , ' de marzo')
else:
    dia = dia - 31
    print('El día de pascua es el ', dia , ' de abril')
