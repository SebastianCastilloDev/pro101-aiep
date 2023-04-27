n = 7
linea = ''
valor = 0
for i in range(n):
    if i <= (n-1)/2:
        for j in range(n):
            if j <= (n-1)/2:
                valor = valor + 1
    else:
        valor = valor - 1
    linea = linea + str(valor)

print(linea)
