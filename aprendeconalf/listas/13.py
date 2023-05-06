# Ejercicio 13 Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

numeros = [2, 3, 4, 2, 2, 3, 4, 2, 2, 3, 4, 2, 2, 2, 2, 4, 6, 67, 8, 89, 6]

longitud = 0

for i in numeros:
    longitud += 1

suma = 0
for i in range(longitud):
    suma += numeros[i]

media = suma/longitud
print('la media es: '+str(media))

suma = 0
for i in range(longitud):
    suma += (numeros[i]-media)**2

desviacion = (suma/longitud)**0.5
print('la desviacion tipica es: '+str(desviacion))

suma = 0
for i in range(longitud):
    suma += 1/numeros[i]
armonica = longitud/suma

print('la media armonica es: ' + str(armonica))

producto = 1
for i in range(longitud):
    producto *= numeros[i]
geometrica = producto**(1/longitud)

print('la media geometrica es: ' + str(geometrica))
