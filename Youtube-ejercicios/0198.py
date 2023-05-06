# Python - Ejercicio 198: Alternar la Posición de Dos Palabras Específicas en una Cadena de Caracteres

print('Escriba un texto que incluya las palabras "Python" y "c++"', end="")
palabras = input().split()

for i in range(len(palabras)):
    if 'C++' in palabras[i]:
        palabras[i] = 'Python'
    if 'Python' in palabras[i]:
        palabras[i] = 'C++'

print(*palabras)
