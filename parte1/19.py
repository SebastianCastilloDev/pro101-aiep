n = 5
valor = 1
linea = ''

for i in range(n):
    for j in range(n):
        if i < (n-1)/2:
            valor = valor+i
            if j < (n-1)/2:
                valor = valor+j

        linea = linea + str(valor)
        valor = 1
    print(linea)
    linea = ''
