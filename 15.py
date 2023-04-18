# 15. Escribe un programa que invierta números enteros positivos. El programa actuará de forma cíclica, solicitando un número en cada pasada y, si no es un número negativo, lo invertirá. El programa finaliza cuando se introduce un número negativo. En este caso, se entiende por invertir el dar la vuelta a los dígitos que componen el número (hallar su imagen especular), esto es, el inverso de 3952 es 2593.

numero = 3952

divisor = 1
maximo_divisor = None # variable auxiliar divisible por 10

# Obtencion del maximo divisor (10, 100, 1000, etc)
while numero / divisor > 1:
    divisor = divisor * 10

maximo_divisor = divisor/10


# obteniendo el primer digito
