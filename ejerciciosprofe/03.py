# Haz un programa que vaya leyendo números y mostrándolos por pantalla hasta que el usuario introduzca un número negativo. En ese momento, el programa mostrará un mensaje de despedida y ﬁnalizara su ejecución.

while True:
    numero = input('ingrese un numero: ')
    if int(numero) < 0:
        print('sayonara')
        break
