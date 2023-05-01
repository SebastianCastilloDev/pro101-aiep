# Python - Ejercicio 90: Generar n Cantidad de Números Primos Consecutivos

def generar_primo():
    numero = 2
    yield numero
    while True:
        temp = numero
        while True:
            temp += 1
            contador = 1
            contador_divisores = 0

            while contador <= temp:
                if temp % contador == 0:
                    contador_divisores += 1
                if contador_divisores > 2:
                    break
                contador += 1

            if contador_divisores == 2:
                yield temp


n = 10
g = generar_primo()
primos = [next(g) for _ in range(n)]

print(primos)
