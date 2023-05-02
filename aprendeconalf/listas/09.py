# Ejercicio 9: Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# frase = input('Ingrese una palabra')
frase = 'sebastian'


def contarvocal(vocal, palabra):
    if vocal in palabra.lower():
        contador = 0
        for letra in palabra.lower():
            if letra == vocal:
                contador += 1
        return (vocal, contador)


vocales = ['a', 'b', 'c', 'd', 'e']

[print(contarvocal(v, 'Sebastian')) for v in vocales]
