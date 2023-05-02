# Python - Ejercicio 149: Calcular la Suma del Cubo de cada Número Menor a un Número n Dado

n = 5

suma = 0
for i in range(n):
    suma += i**3
print(suma)

# otra forma

print(sum([i**3 for i in range(5)]))
