# 3. Crear un programa que pida un numero y muestre la tabla de multiplicar correspondiente a dicho número (hasta 12).

print('Programa que genera la tabla de multiplicar, hasta 12, dado un numero')
n = int(input('Ingrese un numero: '))

i = 1
print('------------------------------')
print('------- Tabla del ', n , '--------')
print('------------------------------')

while i <= 12:
    print(n, ' x ', i , ' = ', n * i)
    i = i + 1