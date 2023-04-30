# comprobar si un caracter es una vocal


def es_vocal(v):
    vocales = 'aeiou'
    if (len(v) == 1):
        v = v.lower()
        return v in vocales
    else:
        return False


print(es_vocal('A'))
print(es_vocal('ae'))
