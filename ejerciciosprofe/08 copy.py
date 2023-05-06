# Una palabra es “alfabética” si todas sus letras están ordenadas alfabéticamente. Por ejemplo:  amor, chino e himno son palabras “alfabéticas”.  Diseña un programa que lea una palabra y nos diga si es alfabética o no

palabra = 'ama'
longitud = 0

for letra in palabra:
    longitud += 1


def es_alfabetica(palabra):
    contador = 0  # cuenta las veces en que la letra es mayor que la siguiente
    for i in range(1, longitud):
        if palabra[i-1] >= palabra[i]:
            contador += 1

    if contador > 0:
        return 'La palabra no es alfabetica'
    else:
        return 'La palabra es alfabetica'


print(es_alfabetica('amor'))
print(es_alfabetica('chino'))
print(es_alfabetica('himno'))
print(es_alfabetica('ama'))
