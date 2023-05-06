# Python - Ejercicio 177: Encontrar los Dígitos Faltantes entre (0-9) de un Número

# Ejemplo]: "232322341" faltan 567890

def encontrar_numeros_faltantes(numero):
    if isinstance(numero, str):
        try:
            numero = int(numero)
            if numero > 0:
                digitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
                numero = {int(d) for d in str(numero)}
                digitos_faltantes = digitos.difference(set(numero))
                return digitos_faltantes
            else:
                raise ValueError('El numero debe ser positivo')
        except:
            raise ValueError('El argumento no es un numero')
    else:
        raise TypeError('El argumento no es una cadena de caracteres')


print(encontrar_numeros_faltantes('12321'))
