# Python - Ejercicio 181: Calcular la Suma de los Dígitos de Dos Números

numeros = [12, 13]


def suma_digitos_numeros(numero1, numero2):
    suma1 = sum([int(c) for c in str(numero1)])
    suma2 = sum([int(c) for c in str(numero2)])
    return (suma1+suma2)


print(suma_digitos_numeros(numeros[0], numeros[1]))
