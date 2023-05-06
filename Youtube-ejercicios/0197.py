# Python - Ejercicio 197: Decir si Dos Lados Adyacentes y una Diagonal son parte de un Paralelogramo
# determinar si dos lados adyacentes y la diagonal de un paralelogramio corresponden a un rectangulo o un rombo

print('Escriba las longitudes de dos lados adyacentes y la diagonal: ', end='')

lado1, lado2, diagonal = map(int, input().split(','))

if diagonal == (lado1**2+lado2**2)**0.5:
    print('Rectangulo')
else:
    print('rombo')
