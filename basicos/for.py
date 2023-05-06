n_caracteres = int(input('Ingrese el numero de caracteres esperados: '))
palabra = input('ingrese una palabra')

contador = 0

# contar caracteres
for letra in palabra:
    contador += 1
# comparacion entre el numero de caracteres ingresados y el numero de caracteres de la palabra
if n_caracteres == contador:
    print('Bkn, le achuntaste')
else:
    print('No cachay na')
