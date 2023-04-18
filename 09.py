# 9. Elaborar un programa para calcular la calificación final de un alumno teniendo como datos 4 calificaciones parciales

nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))
nota3 = float(input("Nota3: "))
nota4 = float(input("Nota4: "))

# Nota final igual al promedio
notafinal = (nota1 + nota2 + nota3 + nota4)/4
print("Nota final: ", notafinal)