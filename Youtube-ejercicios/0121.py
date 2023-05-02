# Python - Ejercicio 121: Determinar si una Variable Está Definida o No

# x =1
try:
    division = 5/x
except NameError as e:
    print('No se puede realizar la operacion:', e.args)
else:
    print('La operacion se realizo de forma satisfactoria')
