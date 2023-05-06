# Python - Ejercicio 202: Obtener el Numerador y el Denominador de un Objeto Fraction

from fractions import Fraction

tres_medios = Fraction(3, 2)

numerador = tres_medios.numerator
denominador = tres_medios.denominator

print(numerador, denominador)
