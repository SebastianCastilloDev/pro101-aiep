# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario

# Ejercicio similar al 09.py

# En este caso lo resolveré utilizando un bucle for in range

suma = 0
for i in range(4):
    nota = float(input('Ingrese nota ' + str(i+1) + ':'))
    suma = suma + nota

promedio = suma/(i+1)

print('El promedio es: ', promedio)