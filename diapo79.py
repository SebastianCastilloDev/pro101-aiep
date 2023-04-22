numero1 = int(input('Ingrese numero1: '))
numero2 = int(input('Ingrese numero2: '))

i = numero1 + 1 # i = 2
total = 0
texto = ''

while i < numero2:
    total = total + i
    if i < numero2-1:
        texto = texto + str(i) + '+'
    elif i == numero2-1:
        texto = texto + str(i)
    i = i + 1

print(texto, ' = ', total)

# print('Resultado= ', total)
