# Python - Ejercicio 153: Eliminar Cada i-ésimo Elemento de una Lista

i = 2  # i esimo

# desde el inicio


def eliminador(lista, iesimo=2):
    longitud = len(lista)
    if longitud > 0:
        cantidad_eliminar = longitud//iesimo
        iesimo -= 1
        indice = 0
        while cantidad_eliminar > 0:
            indice = (iesimo+indice) % longitud
            lista.pop(indice)
            longitud -= 1
            cantidad_eliminar -= 1
    return (lista)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iesimo = 11
print(eliminador(lista, iesimo))
