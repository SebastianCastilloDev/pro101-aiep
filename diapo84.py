# Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda.
# Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.
# Escriba un programa que indique si el número ingresado es o no palíndromo


def invertir(n):
    invertido = ''
    grado = 0
    divisor = 1
    while n / divisor > 1:
        divisor = divisor * 10
        grado = grado + 1
    while grado >= 1:
        grado = grado - 1
        digito = round(n / (10**grado) - (n % (10**grado)) / (10**grado))
        digito = int(digito)
        n = n - digito*(10**grado)
        invertido = str(digito) + invertido
    return int(invertido)


numero = int(input('Ingrese un numero: '))
if numero == invertir(numero):
    print('El numero', numero, 'es palindromo')
else:
    print('El numero', numero, 'no es palindromo')
