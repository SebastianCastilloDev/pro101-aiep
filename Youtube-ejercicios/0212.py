# Python - Ejercicio 212: Parte 1/2: Sumar Filas y Columnas de una Matriz y Crear Matriz Resultante

def print_matriz(matriz):
    for i in range(len(matriz)):
        linea = ''
        for j in range(len(matriz[i])):
            linea += str(matriz[i][j]) + ' '
        print(linea)


def calcular_totales_matriz(matriz):
    for i in range(len(matriz)):
        total_fila = 0
        for j in range(len(matriz[i])):
            total_fila += matriz[i][j]
        matriz[i].append(total_fila)
    total_columnas = []
    for j in range(len(matriz[0])):
        total_columna = 0
        for i in range(len(matriz)):
            total_columna += matriz[i][j]
        total_columnas.append(total_columna)
    matriz.append(total_columnas)


matriz = [[25, 69, 51, 26], [68, 35, 29, 54],
          [54, 57, 45, 63], [61, 68, 47, 59]]
print_matriz(matriz)
calcular_totales_matriz(matriz)
print_matriz(matriz)
