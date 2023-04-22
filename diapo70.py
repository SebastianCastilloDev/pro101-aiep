# Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

# en este caso lo haremos utilizando un bucle for in range

n = int(input('Ingrese un numero: '))

for i in range(10):
    print(n,'x', i+1,'=',n*(i+1))