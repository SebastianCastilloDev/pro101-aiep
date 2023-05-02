# Una palabra es “alfabética” si todas sus letras están ordenadas alfabéticamente. Por ejemplo:  amor, chino e himno son palabras “alfabéticas”.  Diseña un programa que lea una palabra y nos diga si es alfabética o no


palabra = 'amor'

lista = list(palabra)
lista.sort()

nueva_palabra = ''

for char in lista:
    nueva_palabra += char

if nueva_palabra == palabra:
    print('la palabra: ', palabra, 'es alfabetica')
else:
    print('la palabra: ', palabra, 'NO es alfabetica')
