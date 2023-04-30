# Python - Ejercicio 45: Ejecutar un Comando Externo por medio de la Función call

from subprocess import call

print(call(['ping', 'google.com']))
