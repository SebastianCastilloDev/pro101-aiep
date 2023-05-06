# Python - Ejercicio 199: Parte 1/2 - Diferencia entre el Menor y Mayor de un Número de 9 Dígitos

# soluciom:
# numero = 67842213
# mayor = 87643221
# mayor = 12234678
# dif = abs(mayor-menor)

numero = ''

while len(numero) != 9:
    numero = input('Digite un numero de 9 digitos')

    try:
        int(numero)
    except ValueError as e:
        print('Mensaje: Debe digitar un numero')
        numero = ""

digitos = list(numero)

menor = sorted([int(n) for n in digitos])
mayor = sorted([int(n) for n in digitos], reverse=True)

menor = int(''.join([str(d) for d in menor]))
mayor = int(''.join([str(d) for d in mayor]))

print('diferencia: ' + str(abs(mayor-menor)))
