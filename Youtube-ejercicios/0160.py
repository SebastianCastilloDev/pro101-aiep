# Python - Ejercicio 160: Mostrar el Listado de Todos los Módulos Instalados Localmente

import pkg_resources

modulos = pkg_resources.working_set

modulos = sorted([(i.key, i.version) for i in modulos])

print(modulos)

for m in modulos:
    print(m)
