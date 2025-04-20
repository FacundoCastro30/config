#las herencias permiten tomar las caracteristicas de una clase y usarlas en otra. como en otros lenguajes se habla de parent/children, o tambien se les dicen base/derivadas

class person:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def datos(self):
        print(f"{self.nombre} {self.apellido}, {self.edad} años")

f = person("Facundo", "Castro", 36)
f.datos()

#para crear una clase derivada, pasamos como parametro la clase base al crearla

class student(person):
    pass #en este caso es para no agregarle nada mas

l = student("Lucia", "Molina", None )
l.datos()

#si usamos __init__() en la clase derivada, cancela lo recibido de la clase base

"""
esto cancela todo lo recibido: 

class student(person):
    def __init__(self, nombre, apellido, edad)
        self.nombre = nombre
        self.apllido = apellido
        self.edad = edad
"""

#para mantener lo heredado debemos hacerlo como metodo

class estudiante(person):
    def __init__(self, nombre, apellido, edad):
        person.__init__(self, nombre, apellido, edad)
    def __str__(self):
        return (f"{self.nombre} {self.apellido}, {self.edad} años")

n = estudiante("Noeli", "Castro", 29)
print(n)

#si usamos super(), no hace falta poner el nombre de la clase base, y heredad metodos/propiedades

class alumno(person):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
    def __str__(self):
        return (f"{self.nombre} {self.apellido}, {self.edad} años")

r = alumno("Reynado", "Castro", 64)
print(r) 

#agregar caracteristicas: se hace dentro de la misma clase luego de la herencia

class egresado(person):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.anioegreso = 2006
    def __str__(self):
        return (f"{self.nombre} {self.apellido}, {self.edad} años, egresado en {self.anioegreso}")

j = egresado("Jonathan", "Petrini", 36)
print(j.anioegreso)

#lo mismo, si se declara un parametro, se puede pasar

class egresado(person):
    def __init__(self, nombre, apellido, edad, anioegreso):
        super().__init__(nombre, apellido, edad)
        self.anioegreso = anioegreso
    def __str__(self):
        return (f"{self.nombre} {self.apellido}, {self.edad} años, egresado en {self.anioegreso}")

a = egresado("Jonathan", "Amarillo", 36, 2006)
print(a)

#tambien se pueden agregar metodos. al hacerlo, si vien algun metodo heredado y luego se agrega en la derivada, queda cancelado el primero

class profesor(person):
    def __init__(self, nombre, apellido, edad, anioegreso):
        super().__init__(nombre, apellido, edad)
        self.anioegreso = anioegreso
    def __str__(self):
        return (f"{self.nombre} {self.apellido}, {self.edad} años, egresado en {self.anioegreso}")
    def saludo(self):
        print(f"bienvenido, profesor {self.nombre} {self.apellido}")

g = profesor("Gustavo", "Maidana", 36, 2020)
print(g)
g.saludo()