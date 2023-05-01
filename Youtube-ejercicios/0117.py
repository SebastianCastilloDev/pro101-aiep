# Python - Ejercicio 117: Validar que Dos Cadenas de Caracteres Tienen la Misma Ubicación en Memoria

lenguaje = 'Python'

frase = 'Python es tremendo!'

print(hex(id(lenguaje)))
print(hex(id(frase)))

lenguaje += '3'
print(hex(id(lenguaje)))
