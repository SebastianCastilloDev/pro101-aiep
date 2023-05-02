# Haz un programa que vaya leyendo números hasta que el usuario introduzca un número negativo. En ese momento, el programa mostrará por pantalla el número mayor de cuantos ha visto

mayor = 0

while True:
    numero = int(input('ingrese un numero: '))
    if numero < 0:
        break
    if numero > mayor:
        mayor = numero

print('el mayor es el numero ingresado es:', mayor)
