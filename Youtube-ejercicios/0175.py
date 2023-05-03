# Python - Ejercicio 175: Reducir un Número por medio de la Suma de sus Dígitos

# obtener un entero positivo y sustraer la suma de sus digitos mientra el numero sea positivo y mostrar el numero de iteraciones necesarias

def reducir_numero(n):
    cadena = str(n)
    contador = 0
    while n > 0:
        n -= sum([int(c)for c in cadena])
        cadena = str(n)

        contador += 1
    return contador


print(reducir_numero(7))
print(reducir_numero(29))
