# Python - Ejercicio 69: Ordenar Tres Números de Menor a Mayor sin Usar Condicionales ni Ciclos

x = int(input('Escriba numero 1: '))
y = int(input('Escriba numero 2: '))
z = int(input('Escriba numero 3: '))

# minimo
a = min(x, y, z)
# maximo
c = max(x, y, z)

# intermedio
b = (x+y+z)-(a+c)

print([a, b, c])
