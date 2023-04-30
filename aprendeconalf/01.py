# https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

ingreso = True

asignaturas = []

while ingreso:
    asignatura = input('Ingrese una asignatura: ')
    if asignatura == '':
        ingreso = False
    else:
        asignaturas += [asignatura]

print(asignaturas)
