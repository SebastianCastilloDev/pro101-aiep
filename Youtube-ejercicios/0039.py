# Calcular el Valor Futuro de una Cantidad, Interés y Años Específicos

# vf = va*(1+i)^n

# vf: valor futuro
# va: valor actual
# i: interes
# n: años especificos

def vf(va, i, n):
    return va*(1+i)**n


print(vf(100000, 0.05, 3))
