# Python - Ejercicio 156: Contar el Número de Ocurrencias de las Palabras en una Frase o Párrafo

cadena = """
El código del ejercicio 16 en Python es el siguiente: # -*- coding: utf-8 -*- #Decoración: Nombre del Algoritmo print("-------------------------------------------------------") print("Ejercicio16: DETERMINA LA SALIDA.") print("-------------------------------------------------------") #Entradas A = int( input("Ingrese A: ")) B = int( input("Ingrese B: ")) C = int( input("Ingrese C: ")) print("\nSALIDA: ") print("-------------------------------------------------------")
#Proceso if A > B : if A > C: if B > C: print(A, B, C) else: print(A,C,B) else: print(C,A,B) else: if B > C : if A > C : print(B,A,C) else: print(B,C,A) else: print(C,B,A)
------------------------------------------------------- Ejercicio16: DETERMINA LA SALIDA. ------------------------------------------------------- Ingrese A: 2 Ingrese B: 90 Ingrese C: 45 SALIDA: ------------------------------------------------------- 90 45 2 4.4 Ejercicios complementarios
1. Construya un algoritmo que, dados tres números, muestre el mensaje “IGUALES” si la suma de los dos primeros es igual al otro número y el mensaje “DISTINTOS” en caso contrario.
Algoritmos resueltos con Python ISBN: 978-958-53018-2-5 126 / 257
Pseudocódigo.
Algoritmo igdis
Var
a,b,c: entero
Inicio
Escribir ("Ingrese tres números:")
Leer (a,b,c)
Si (a+b=c) entonces
Escribir ("IGUALES")
sino
Escribir ("DISTINTOS")
Fin Si
Fin
Diagrama de Flujo.
IInniicciioo
FFiinn
"Ingrese tres
números:"
aa,,bb,,cc
aa++bb==cc
""IIGGUUAALLEESS"" ""DDIISSTTIINNTTOOSS""
V
V F
F
Algoritmos resueltos con Python ISBN: 978-958-53018-2-5 127 / 257
El código del complementario 1 en Python es el siguiente: # -*- coding: utf-8 -*- #Decoración: Nombre del Algoritmo print("-------------------------------------------------------") print("Complemento1: IGUALES O DISTINTOS.") print("-------------------------------------------------------") #Entradas print("Ingrese tres números") a = int( input("Ingrese a: ")) b = int( input("Ingrese b: ")) c = int( input("Ingrese c: ")) #Salida print("\nSALIDA: ") print("-------------------------------------------------------") if a + b == c : print("IGUALES") else: print("DISTINTOS")
------------------------------------------------------- Complemento1: IGUALES O DISTINTOS. ------------------------------------------------------- Ingrese tres números Ingrese a: 10 Ingrese b: 5 Ingrese c: 15 SALIDA: ------------------------------------------------------- IGUALES
2. Algoritmo, que dado dos números “a” y “b”, muestre sus valores en orden de menor a mayor.
Algoritmos resueltos con Python ISBN: 978-958-53018-2-5 128 / 257
Pseudocódigo.
Algoritmo orden_creciente
Var
a,b: entero
Inicio
Escribir ("Ingrese dos números:")
Leer a,b
Si (a<b) entonces
Escribir ("Los números son: ",a," , ",b)
sino
Escribir ("Los números son: ",b," , ",a)
Fin Si
Fin
Diagrama de Flujo.
Inicio
Fin
"Ingrese dos
números:"
a,b
a<b
"Los números son: ",a," , ",b "Los números son: ",b," , ",a
V F
Algoritmos resueltos con Python ISBN: 978-958-53018-2-5 129 / 257
El código del complementario 2 en Python es el siguiente:
# -*- coding: utf-8 -*- #Decoración: Nombre del Algoritmo print("-------------------------------------------------------")
"""

palabras = cadena.split(' ')
frecuencia_palabras = [palabras.count(p) for p in palabras]

print(str(list(zip(palabras, frecuencia_palabras))))
