# Python - Ejercicio 101: Acceder a una URL e Imprimir su Contenido HTML

from http.client import HTTPConnection

url = 'example.com'

conexion = HTTPConnection(url)
conexion.request('GET', '/')
respuesta = conexion.getresponse()
contenido = respuesta.read()
print(contenido)
