# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = []
continua = True

while continua:
    asignatura = input('Ingrese asignatura: ')
    if (asignatura == ""):
        continua = False
    else:
        asignaturas = asignaturas + [asignatura]

for asignatura in asignaturas:
    print('Yo estudio el curso de: ' + asignatura)
