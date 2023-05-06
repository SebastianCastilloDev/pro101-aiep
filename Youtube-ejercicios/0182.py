# Python - Ejercicio 182: Determinar el Tipo de Triángulo (Isósceles, Escaleno, Equilatero)


def tipo_triangulo(a, b, c):
    if a == b == c:
        return 'equilatero'
    elif a != b and a != c:
        return 'escaleno'
    else:
        return 'isosceles'
