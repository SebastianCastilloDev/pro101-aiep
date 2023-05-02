# Python - Ejercicio 170: Encontrar el Valor de posicion Media Entre Tres Números

# 3,9,7

x = int(input('ingrese n: '))
y = int(input('ingrese n: '))
z = int(input('ingrese n: '))

# solucion 1

menor = min(x, y, z)
mayor = max(x, y, z)
medio = (x+y+z)-menor-mayor

# solucion 2

nums = [x, y, z]
nums.sort()
print(nums[1])
