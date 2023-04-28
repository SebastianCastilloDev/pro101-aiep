# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas = []
notas = []
continua = True

while continua:
    asignatura = input('Ingrese asignatura: ')
    nota = input('Ingrese nota: ')

    if (asignatura == ""):
        continua = False
    else:
        asignaturas = asignaturas + [asignatura]
        notas = notas + [nota]

i = 0
while (i < len(asignaturas)):
    print('En ' + asignaturas[i]+' has sacado nota: ' + notas[i])
    i = i+1
