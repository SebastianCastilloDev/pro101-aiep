# Escribir un programa que pregunte la edad de esa persona y determine el año de nacimiento.

import datetime

edad = int(input("Ingrese su edad: "))
anio_actual = datetime.datetime.now().year
anio_nacimiento = anio_actual - edad
print ("Año de nacimiento: " + str(anio_nacimiento))