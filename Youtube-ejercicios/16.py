# calcular con condiciones
# fn(n): si n <= 15 -> 15-n; (15-n)*2

def funcion(n):
    if n <= 15:
        return 15 - n
    else:
        return (15-n)*2


print(funcion(15))
