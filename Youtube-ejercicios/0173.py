# " Python - Ejercicio 173: Calcular la Cantidad Mínima de Monedas para el Cambio de una Compra

def calcular_cantidad_min_cambio(monto):
    nominaciones = [500, 100, 50, 10]  # monedas

    monedas = 0

    for i in range(len(nominaciones)):
        nominacion = nominaciones[i]
        monedas += int(monto/nominacion)
        monto = int(monto % nominacion)
    return monedas


print(calcular_cantidad_min_cambio(550))
