# 13. Escribe un programa que lea una temperatura introducida a travÃ©s de teclado y muestre por pantalla la actividad más apropiada para dicha temperatura teniendo en cuenta los siguientes criterios.

# **ACTIVIDAD TEMPERATURA IDONEA**
# * Natación temp > 30
# * Tenis 20 < temp <= 30
# * Golf 10 < temp <= 20
# * Esquí 5 < temp <= 10

temperatura = float(input('Ingrese Temperatura: '))

if temperatura > 30:
    actividad = "Natacion"
elif temperatura <= 30 and temperatura > 20:
    actividad = "Tenis"
elif temperatura <= 20 and temperatura > 10:
    actividad = "Golf"
elif temperatura <= 10 and temperatura > 5:
    actividad = "Esqui"
else:
    actividad =  "No hay actividad recomendada"

print('La actividad recomendada es: ', actividad)