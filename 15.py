# 15. Escribe un programa que invierta números enteros positivos. El programa actuará de forma cíclica, solicitando un número en cada pasada y, si no es un número negativo, lo invertirá. El programa finaliza cuando se introduce un número negativo. En este caso, se entiende por invertir el dar la vuelta a los dígitos que componen el número (hallar su imagen especular), esto es, el inverso de 3952 es 2593.

#14,41, 19
numero = 411112331
invertido = ''

grado = 0

divisor = 1

while numero / divisor > 1 :
    divisor = divisor * 10
    grado = grado + 1
print('divisor: ', divisor)
print('grado: ', grado)


while (grado >= 1):
    grado = grado - 1
    print('grado: ', grado)

    digito = round(numero / (10**grado) - (numero % (10**grado)) / (10**grado))
    digito = int(digito)
    print('digito: ', digito)
    
    numero = numero - digito*(10**grado)
    print('numero: ', numero)

    invertido = str(digito) + invertido
    print('invertido: ', invertido)

