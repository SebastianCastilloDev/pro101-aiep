# Calcular la suma de 3 numeros si todos son diferentes, en caso contrario la suma será cero.

def sumaespecial(a, b, c):
    if a == b and a == c:
        return 0
    else:
        return a+b+c


print(sumaespecial(3, 3, 3))
print(sumaespecial(3, 3, 4))
