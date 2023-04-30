# Sumar Dos Números. Si la Suma se Halla entre 10 y 30, Retornar 30

def suma(a, b):
    res = a+b
    if res >= 10 and res <= 30:
        return 30
    else:
        return res


print(suma(20, 4))
print(suma(20, 30))
