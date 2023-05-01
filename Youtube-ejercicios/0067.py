# Python - Ejercicio 67: Convertir kilopascales (kPa) en presión psi, mmHg, y atm

kpa = float(input('ingrese kpa: '))

psi = kpa/6.89475729
mmhg = kpa*760/101.325
atm = kpa / 101.325
