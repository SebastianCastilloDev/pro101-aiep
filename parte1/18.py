# 18. Escribir un programa que muestre las tablas de multiplicar para todos los números entre dos números introducidos por el usuario.
# Es decir, si el usuario solicita las tablas entre 2 y 5, el programa mostrará las tablas completas del 2, el 3, el 4 y el 5.

numero1 = int(input('Numero1: '))
numero2 = int(input('Numero2: '))

i = numero1

while i <= numero2:
    print('Tabla del: ', i)
    j = 1
    while j <= 10:
        print(i, ' x ', j, ' = ', i*j)
        j = j + 1
    print('-------------------------')
    i = i + 1