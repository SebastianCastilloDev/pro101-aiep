# Python - Ejercicio 137: Extraer un Único Elemento (Llave y Valor) de un Diccionario

lenguajes = {'Python': '3', 'Java': '12', 'c#': '8', 'PHP': '8'}

(lenguaje, version), _, (csharp, versioncsharp), _ = lenguajes.items()

print(lenguaje, version)
print(csharp, versioncsharp)
