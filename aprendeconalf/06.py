
# Ejercicio
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

aprobados = []
reprobados = []
notas = []

for asignatura in asignaturas:
    nota = int(input('Ingrese la nota para ' + asignatura + ':'))
    notas += [nota]
    if nota >= 4.0:
        aprobados += [asignatura]
    else:
        reprobados += [asignatura]

print('los ramos a repetir son:' + str(reprobados))
