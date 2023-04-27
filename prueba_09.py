""" Conversion """


def hex_bin(n):
    """ Conversion """
    if n == 0:
        binario = '0000'
    elif n == 1:
        binario = '0001'
    elif n == 2:
        binario = '0010'
    elif n == 3:
        binario = '0011'
    elif n == 4:
        binario = '0100'
    elif n == 5:
        binario = '0101'
    elif n == 6:
        binario = '0110'
    elif n == 7:
        binario = '0111'
    elif n == 8:
        binario = '1000'
    elif n == 9:
        binario = '1001'
    elif n in ('A', 'a'):
        binario = '1010'
    elif n in ('B', 'b'):
        binario = '1011'
    elif n in ('C', 'c'):
        binario = '1100'
    elif n in ('D', 'd'):
        binario = '1101'
    elif n in ('E', 'e'):
        binario = '1110'
    elif n in ('F', 'f'):
        binario = '1111'
    return binario
