# generar lo n primeros pares positivos

def generar_numeros_pares(n):
    pares = []
    for i in range(1, 2*n+1):
        if i % 2 == 0:
            pares.append(i)
    return (pares)


print(generar_numeros_pares(6))
