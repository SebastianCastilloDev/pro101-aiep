# Python - Ejercicio 162: Determinar si la Suma de los Elementos de una Lista es Igual a un Número

def suma_igual(numero, numeros):
    return sum(numeros) == numero


lista = (8, 9, 2)
lista = [2, 3, 43, 4, 5, 3, 32]

total = 19

print(suma_igual(total, lista))
