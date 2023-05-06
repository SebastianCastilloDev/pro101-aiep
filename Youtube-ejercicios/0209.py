# Python - Ejercicio 209: Obtener Sólo las Palabras de Longitud de 3 a 6 Caracteres

cadena = 'Esta es una cadena pero no incluye palabras con longitudes menores a 3 caracteres o mayores a seis caracteres'

palabras = cadena.split(' ')
print(palabras)
palabras3a6 = []
for palabra in palabras:
    if len(palabra) >= 3 and len(palabra) <= 6:
        palabras3a6 += [palabra]
print(palabras3a6)
