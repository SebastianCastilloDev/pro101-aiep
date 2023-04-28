# Escriba una programa que permita determinar el número mayor pertenecientes a un conjunto de n números, donde el valor de n como los números deben ser ingresados por el usuario

n = int(input('Cuantos numeros quiere ingresar? '))

mayor = 0
i = 0
while i < n:
    numero = int(input('Ingrese el numero ' + str(i+1) + ': '))
    if numero > mayor:
        mayor = numero
    i = i + 1

print('El numero mayor es: ', mayor)

