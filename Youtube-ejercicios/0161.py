# Python - Ejercicio 161: Obtener Información del Sistema Operativo donde se Ejecuta un Script Python

import platform

perfil_so = [
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',
]

for perfil in perfil_so:
    if hasattr(platform, perfil):
        print(perfil, getattr(platform, perfil)())
