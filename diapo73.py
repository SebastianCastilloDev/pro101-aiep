
n = int(input('ingrese un numero de 3 digitos'))

grado = 3
invertido = ''
for i in range(3):
    grado = grado -1

    digito = round(n / (10**grado) - (n % (10**grado)) / (10**grado))
    digito = int(digito)
    print('digito: ', digito)
    
    n = n - digito*(10**grado)
    print('numero: ', n)

    invertido = str(digito) + invertido
    print('invertido: ', invertido)