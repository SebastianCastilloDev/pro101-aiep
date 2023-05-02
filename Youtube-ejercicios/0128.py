# Python - Ejercicio 128: Comprobar si un Carácter Específico se Encuentra en una Cadena de Caracteres

texto = 'este Es un texto'
print(texto.count('y') > 0)
print(texto.count('e') > 0)

print(any(c == 'y' for c in texto))
print(any(c == 'e' for c in texto))

print(texto.count('E') > 0)
print(texto.count('e') > 0)

print(any(c.lower() == 'e' for c in texto))
