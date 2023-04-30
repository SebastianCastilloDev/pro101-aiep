# obtener un conjunto de numeros separados por coma y crear una lista

numeros = input('Ingrese una lista de valores separados por coma: ')

lista = numeros.replace(' ', '').split(',')
print(lista)
