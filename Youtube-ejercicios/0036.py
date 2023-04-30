# Python - Ejercicio 36: Crear una Clase para Representar los Datos de una Persona

class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nCorreo: {}'.format(self.nombre, self.edad, self.correo)


sebastian = Persona('Sebastian', '39', 'correo')

print(sebastian)
print(sebastian.nombre)
print(sebastian.edad)
