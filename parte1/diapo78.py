# Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor
# Modifique para que el programa ordene cuatro números
a = int(input('Ingrese un numero: '))
b = int(input('Ingrese otro numero: '))

if a >= b:
    print (a,',',b)
if a < b:
    print (b,',',a)


#----------------------------------------------------------------

a = int(input('Ingrese numero1: '))
b = int(input('Ingrese numero2: '))
c = int(input('Ingrese numero3: '))
d = int(input('Ingrese numero4: '))

menor = 0

if a <= b and a <= c and a <= d:
    menor = a
elif b <= a and b <= c and b <= d:
    menor = b
elif c <= a and c <= b and c <= d:
    menor = c
else:
    menor = d

print(menor, ',')

# Repetimos el proceso entre los tres restantes
    