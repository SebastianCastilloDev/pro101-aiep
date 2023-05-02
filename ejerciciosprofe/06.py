# Modifique el programa anterior para que lea el número de caracteres esperados, y posteriormente lea una palabra e indique si el número de caracteres corresponde al número de caracteres esperados.

palabra = input('ingrese palabra: ')
caracteres = int(input('ingrese el numero de caracteres: '))

chars = 0

for char in palabra:
    chars += 1

if chars == caracteres:
    print('Correcto, la palabra', palabra, 'tiene', chars, 'caracteres')
else:
    print(palabra, 'no tiene', caracteres,
          'caracteres ---', 'tiene', chars, 'caracteres')
