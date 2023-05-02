# Implementa un programa que muestre todos los números potencia de 2 entre 2^0 y 2^30, ambos inclusive.
n = 30
[print("2^"+str(i)+" = " + str(2**i)) for i in range(n+1)]
