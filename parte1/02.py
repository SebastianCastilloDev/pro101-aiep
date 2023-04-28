# 2. Escribir un programa que pregunte el año actual y la edad de una persona y calcule la edad de esa persona en un año determinado.


edad = int(input('ingrese su edad: '))
anio_actual = int(input('ingrese el año actual: '))
anio_base = int(input('Ingrese el año base (para calcular edad): '))

anio_nacimiento = anio_actual - edad

edad_anio_base = anio_base - anio_nacimiento

print ('Tu edad en el año: ', anio_base, ' es de: ', edad_anio_base, ' años')