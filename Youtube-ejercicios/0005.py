# representacion inversa de una cadena

cadena = 'Python'

for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end='')

print(cadena[0:len(cadena):-1])
print(cadena[::-1])
