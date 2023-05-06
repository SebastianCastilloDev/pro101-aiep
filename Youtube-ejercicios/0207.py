# Python - Ejercicio 207: Restaurar un Texto a partir de la Versión Acortada del Texto

# a#b3 = abbb

def restaurar_texto(acortado):

    resultado = ''
    indice = 0
    longitud = len(acortado)

    while indice < longitud:
        if acortado[indice] == "#":
            resultado += acortado[indice+2]*int(acortado[indice+1])
            indice += 3
        else:
            resultado += acortado[indice]
            indice += 1
    return (resultado)


print(restaurar_texto('a#3b'))
