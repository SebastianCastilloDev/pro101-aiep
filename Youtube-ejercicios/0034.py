# Python - Ejercicio 34: Validar dos Números. Si son Iguales o la Suma o el Valor Absoluto son 5

def validarNumeros(a, b):
    if a == b or (a + b) == 5 or abs(a-b) == 5:
        return True
    else:
        return False


print(validarNumeros(3, 3))
print(validarNumeros(5, 7))
print(validarNumeros(11, 16))
print(validarNumeros(4, 1))
