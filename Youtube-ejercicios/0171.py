# Python - Ejercicio 172: Explorar el Nuevo Soporte para Depuración por medio de f-strings

# (248163264128)=7
# (248163264)=6
# (2481632)=5

def encontrar_potencias_2(secuencia):
    respuesta = True
    base = 2
    resultado = 2
    grado = 1
    while respuesta:
        if str(resultado) in secuencia:
            grado += 1
            resultado = pow(base, grado)
        else:
            respuesta = False
    return grado-1


print(encontrar_potencias_2('248'))
print(encontrar_potencias_2('248163264128256'))
