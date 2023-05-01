# Python - Ejercicio 58: Calcular la Suma de los Primeros n Números Enteros

# Usando la formula de Gauss: n*(n+1)/2
n = 10
suma = n*(n+1)/2
print(suma)

# usando un ciclo
suma = 0
for i in range(1, n+1):
    suma = suma + i
print(suma)

# Usar la funcion sum (puede sumar listas)
suma = sum(range(1, n+1))
print(suma)
