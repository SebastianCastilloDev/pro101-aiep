# Haz un programa que lea una palabra e indique cuantos caracteres tiene.

palabra = input('ingrese palabra: ')

chars = 0

for char in palabra:
    chars += 1

print(palabra, 'tiene', chars, 'caracteres')
