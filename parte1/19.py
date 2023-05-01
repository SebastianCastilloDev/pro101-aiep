
n = int(input('ingrese un numero impar: '))

linea = ''

if n % 2 != 0:

    for i in range(n):
        for j in range(n):

            if j < n - (j+1):
                a = j
            else:
                a = n - (j+1)

            if i < n - (i+1):
                b = i
            else:
                b = n - (i+1)

            if a < b:
                if j < n - (j+1):
                    x = j
                else:
                    x = n - (j+1)
            else:
                if i < n - (i+1):
                    x = i
                else:
                    x = n - (i+1)

            linea = linea + str(x+1)
        print(linea)
        linea = ''
else:
    print('Error: El numero ingresado debe ser impar')
