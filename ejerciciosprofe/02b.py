# Haz un programa que muestre, en líneas independientes, todos los números pares comprendidos entre 0 y 200 (ambos inclusive)

n = 200

for i in range(n+1):
    if i % 2 == 0:
        print(i)
