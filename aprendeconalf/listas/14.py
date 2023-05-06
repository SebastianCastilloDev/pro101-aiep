# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def deletrear_palabra_al_verres(palabra):
    palabra_al_reves = ''
    for letra in palabra:
        palabra_al_reves = letra + palabra_al_reves

    for letra in palabra_al_reves:
        print(letra)


########################
palabra = input('Ingrese una palabra')
deletrear_palabra_al_verres(palabra)
