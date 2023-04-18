# 5. Leer tres números y, si el primero de ellos es negativo, calcular el producto de los tres, en caso contrario calcular la suma de ellos.

numero1 = float(input('Ingrese numero1: '))
numero2 = float(input('Ingrese numero2: '))
numero3 = float(input('Ingrese numero3: '))

if numero1 < 0:
    resultado = numero1*numero2*numero3
else:
    resultado = numero1 + numero2 + numero3

print('Resultado = ',resultado)