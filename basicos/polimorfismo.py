#refiere a un metodo, funcion  u operador que puede ser utilizado en dsitintos objetos o clases. un ejemplo es la funcion len()

#un ejemplo de esto se da en clases, donde varias clases distintas pueden compartir un metodo con el mismo nombre

class auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def movete(self):
        print("Manejar")

class bote:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
    def movete(self):
        print("Navegar")

class avion:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo        
    def movete(self):
        print("Volar")        

auto1 = auto("Nissan", "March")
bote1 = bote("Titanic", 1912)
avion1 = avion("Boeing", "747")

for x in (auto1, bote1, avion1):
    x.movete()

#en este caso se ejecuta el metodo en los 3 objetos

#el polimorfismo se da por herencia de manera similar a lo visto, y puede cambiarse lo heredado dentro de las derivadas

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def trabajo(self):
        print("fabrica")

class reynaldo(persona):
    pass

class facundo(persona):
    def trabajo(self):
        print("grabados")

class nora(persona):
    def trabajo(self):
        print("cuidar a Pia")

r = reynaldo("Reynaldo", 64)
f = facundo("Facundo", 36)
n = nora("Nora", 61)

for x in (r, f, n):
    print(x.nombre)
    print(x.edad)
    x.trabajo()

#en este caso la primer clase hereda las caracteristicas dadas en persona, por eso tiene un pass. y en las siguientes, se hereda las primeras pero se sobreescribe el metodo