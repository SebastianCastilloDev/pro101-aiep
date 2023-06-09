# Python - Ejercicio 185: Encontrar los Números Primos Menores a un Número n Específico

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


def primos_menores(n):
    generador = generar_primo()
    primos = []
    while True:
        primo = next(generador)
        if primo < n:
            primos.append(primo)
        else:
            break

    return primos


print(primos_menores(20))
