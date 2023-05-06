# Python - Ejercicio 183: Resolver un Sistema de Ecuaciones Lineales

# ax+by=c
# dx+ey=f

def sist_ec(a, b, c, d, e, f):
    determinante = a*e-b*d
    if determinante != 0:
        x = (c*e-b*f)/determinante
        y = (a*f-c*d)/determinante
        return x, y
    else:
        return None


a, b, c, d, e, f = map(float, input().split())
print(sist_ec(a, b, c, d, e, f))
