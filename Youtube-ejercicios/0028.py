# Calcular la diferencia de conjuntos con colores

colores_lista_1 = ['negro', 'rojo', 'verde', 'blanco']
colores_lista_2 = ['blanco', 'azul', 'verde', 'amarillo']

# A,B,a-b,a/b

colores_conjunto_1 = set(colores_lista_1)
colores_conjunto_2 = set(colores_lista_2)

diferencia = colores_conjunto_1.difference(colores_conjunto_2)

print(diferencia)
