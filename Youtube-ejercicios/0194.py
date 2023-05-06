# Python - Ejercicio 194: Encontrar el Nombre del Día a partir de una Fecha Dada

from datetime import date

print('Ingrese el numero del mes y del dia: ', end='')
mes, dia = map(int, input().split())  # separados por espacio

semana = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles',
          4: 'Jueves', 5: 'viernes', 6: 'Sabado', 7: 'Domingo'}

numero_dia = date.isoweekday(date(2023, mes, dia))

print('nombre del dia es: '+semana[numero_dia])
