# Python - Ejercicio 56: Obtener el Tamaño de la Ventana de la Terminal

import fcntl
import termios
import struct


def calcular_tamano_terminal():
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(
        0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))

    return tw, th


print(calcular_tamano_terminal())
