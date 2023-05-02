#  Python - Ejercicio 167: Calcular el Tercer Lado de un Triángulo Rectángulo Dados Dos de sus Lados

def pitagoras(cateto_adyacente, cateto_opuesto, hipotenusa):
    if cateto_adyacente == 'x':
        return (hipotenusa**2-cateto_opuesto**2)**0.5
    elif cateto_opuesto == 'x':
        return (hipotenusa**2-cateto_adyacente**2)**0.5
    elif hipotenusa == 'x':
        return (cateto_adyacente**2+cateto_opuesto**2)**0.5
    else:
        return None


print(pitagoras(3, 4, 'x'))
