# 10. Escribir un programa que imprima la conversión de kilómetros a millas 
# (1 MILLA MARINA = 1852mts Y 1 MILLA = 1609mts)

medida = float(input('Medida en km'))

medida_milla = medida/1.609
medida_milla_marina = medida/1.852

print ('Medida en millas: ', medida_milla)
print ('Medida en millas marinas: ', medida_milla_marina)