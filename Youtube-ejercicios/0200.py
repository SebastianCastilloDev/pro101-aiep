# Python - Ejercicio 200: Calcular la Suma de los Números Primos Existentes entre 2 y 100
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


suma_primos = 0
generador_primo = generar_primo()

while True:
    primo = next(generador_primo)
    if primo <= 100:
        suma_primos += primo
    else:
        break

print(suma_primos)
