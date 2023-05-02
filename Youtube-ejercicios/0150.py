# Python - Ejercicio 150: Comprobar si Existe al Menos un Producto Impar entre una Lista de Números

l = [2, 3, 4, 5, 6]

for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i]*l[j] % 2 == 1:
            print(True)
            break
        else:
            print(False)
