# Python - Ejercicio 68: Sumar los Dígitos Integrales de un Número Entero  1234 -> 1+2+3+4 = 10

numero = input('Escriba un numero entero positivo: ')

lista_digitos = list(numero)

suma = 0
for digito in lista_digitos:
    suma += int(digito)
print(suma)
# ============================

lista_digitos = [int(c) for c in lista_digitos]
suma = sum(lista_digitos)
print(suma)
