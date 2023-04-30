# Emulal el funcionamiento de join para concatenar una cada

# numeros = [1,5,4,3] -> 1543

def emulajoin(lista):
    texto = ''
    for elemento in lista:
        texto += str(elemento)
    return texto


lista = [2, 3, 4, 5, 56, 61, 2, 322, 2, 2, 3]
print(emulajoin(lista))
