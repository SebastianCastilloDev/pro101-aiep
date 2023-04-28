# 6. Escribir un programa que determine cuantos años bisiesto existen en un periodo dado por el usuario.
# **Nota: Un año bisiesto:**
# * Debe ser divisible por 4, pero no por 100.
# * Debe ser divisible por 400.
# * Por ejemplo, el año 1900 no fue bisiesto, el 2000 sí y el 2100 no lo es
# Existe un operador que permite determinar el resto de una división, por ejemplo: 2 % 2 será igual a cero, mientras que 1 % 2 será igual a 1. El operador es %

anio_inicial = int(input('Ingrese el año inicial: '))
anio_final = int(input('Ingrese el año final: '))

contador_anio = anio_inicial
contador_bisiestos = 0



while contador_anio <= anio_final:
    if(contador_anio % 4 == 0 and contador_anio % 100 != 0) or (contador_anio % (4*100) == 0):
        print('año bisiesto = ', contador_anio)
        contador_bisiestos = contador_bisiestos + 1
    contador_anio = contador_anio + 1

print ('El numero de años bisiestos entre ',anio_inicial, ' y ',anio_final, ' es: ', contador_bisiestos)