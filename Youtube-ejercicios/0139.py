# Python - Ejercicio 139: Validar si una Dirección IP es Válida

import socket


def ip_valida(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


print(ip_valida('127.0.0.1'))
print(ip_valida('127.0.0.1a'))
print(ip_valida('127.0.0.1234'))
