# Python - Ejercicio 37: Crear una Jerarquía de Herencia Básica

class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo


class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera


sebastian = Estudiante('123', 'Sebastian', 'correo', 'carnet', 'programacion')
print(isinstance(sebastian, Estudiante))
print(isinstance(sebastian, Persona))
