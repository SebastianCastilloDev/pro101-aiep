# https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
ingreso = True

asignaturas = []

while ingreso:
    asignatura = input('Ingrese una asignatura: ')
    if asignatura == '':
        ingreso = False
    else:
        asignaturas += [asignatura]

for asignatura in asignaturas:
    print('Yo estudio ' + asignatura)
