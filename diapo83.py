# n = int(input('Ingrese el tamaño de lado del hexágono'))
n = int(input('Ingrese el lado del hexagono: '))
linea = ''

altura = 2*n-1
ancho = 3*n-2

for i in range(altura):
    for j in range(ancho):
        if i < n:
            if (j < n-i-1 or j > ancho-n+i):
                linea = linea + ' '
            else:
                linea = linea + '*'
        else:
            if (j < i-n+1 or j > ancho-i+n-2):

                linea = linea + ' '
            else:
                linea = linea + '*'
            # print(ancho - i+1)
    print(linea)
    linea = ''
