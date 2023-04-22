n = int(input('Ingrese la altura: '))
m = int(input('Ingrese el ancho: '))

linea = ''
caracter = '*'

for i in range(n):
    for j in range(m):
        linea = linea + caracter
    print (linea)
    linea = ''
