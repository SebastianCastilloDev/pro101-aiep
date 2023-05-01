# Python - Ejercicio 104: Obtener el ID de Usuario, Grupo e IDs de Grupos Complementarios

import os
print('El id es', os.geteuid())
print('El id de grupo es', os.getegid())
print('El id de grupo complementario', str(os.getgroups()))
