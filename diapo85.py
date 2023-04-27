# El método de multiplicación rusa consiste en multiplicar sucesivamente por 2 el multiplicando y dividir por 2 el multiplicador hasta que el multiplicador tome el valor 1. Luego, se suman todos los multiplicandos correspondientes a los multiplicadores impares.
# Dicha suma es el producto de los dos números. La siguiente tabla muestra el cálculo realizado para multiplicar 37 por 12, cuyo resultado final es 12 + 48 + 384 = 444.

a = int(input('numero 1:'))
b = int(input('numero 2:'))

total = 0
while (a >= 1):
    if a % 2 != 0:
        total = total + b
    b = b * 2
    a = int(a/2)
print('El resultado es: ', total)
