n = int(input('Ingrese un numero impar'))

i = 0
j = 0
linea = ''
while i < n:
    i = i + 1
    while j < n:
        j = j + 1
        linea = str(i) + linea
    print (linea)