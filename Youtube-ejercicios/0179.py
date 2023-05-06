# Python - Ejercicio 179: Identificar el Tipo de Progresión (Aritmética o Geométrica) de una Lista

def identificar_progresion(numeros):

    if numeros[1]-numeros[0] == numeros[2]-numeros[1]:
        print('Aritmetica')
    elif numeros[1]/numeros[0] == numeros[2]/numeros[1]:
        print('Aritmetica')
    else:
        print('no se q es')
