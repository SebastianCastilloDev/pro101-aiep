# emular producto de cadenas
def producto_cadena(cadena, repeticion):
    resultado = ""
    for i in range(repeticion):
        resultado += cadena
    return resultado


print(producto_cadena('texto', 3))
