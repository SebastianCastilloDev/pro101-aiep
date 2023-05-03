# Python - Ejercicio 174: Calcular el n-ésimo Término de una Secuencia

# secuencia: n = sum(n-1,n-2,n-3,n-4), los primero terminos son 1,1,1,1

total = 0


def secuencia(n):
    if n <= 4:
        return 1
    else:
        return secuencia(n-1)+secuencia(n-2)+secuencia(n-3)+secuencia(n-4)


print(secuencia(7))
