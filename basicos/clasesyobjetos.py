#clases

#Python es un lenguaje orientado a objetos. casi cualquier cosa en python es un objeto y tiene un constructor, que seria como un plano de sus caracteristicas 

class mi_clase:
    x = 5

#donde x seria una caracteristica. con esto se puede crear objetos

o1=mi_clase()
print(o1.x)

#el ejemplo anterior es un ejemplo basico y poco util. la gracia de las clases se da cuando usamos la funcion __init__(). se ejecuta siempre que se crea una clase. sirve para agregar valores a las caracteristicas de un objeto

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = persona("Facundo", 36)

print(f"{p1.nombre} tiene {p1.edad} años de edad")

##con la funcion __str__() controlamos lo que queremos que se lea cuando se representa el objeto

class auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    def __str__(self):
        return (f"{self.marca} de color {self.color}")
    
a1=auto("Nissan", "gris")

print(a1)

#self indica que se esta usando la instancia actual de la clase. puede tener cualquier otro nombre pero tiene que ser el primer parametro siempre

#los objetos pueden tener metodos, que son funciones que pertenecen al mismo

class mascotas:
    def __init__(self, nombre, tutor):
        self.nombre = nombre
        self.tutor = tutor
    def __str__(self):
        return (f"{self.nombre} es la mascota de {self.tutor}")
    def saludo(self):
        print(f"Hola, soy {self.nombre} y mi tutor es {self.tutor}")

m1 = mascotas("Mila", "Lucia")
m1.saludo()

#se pueden modificar las propiedades de un objeto asi (ejemplo de una funcion de linea 26)
 
a1.color = "negro" #el color antes era gris
print(a1)

#con del podemos borrar una propiedad de un objeto o el objeto completo

del a1.color
del a1

#se puede usar pass para no dejar una clase vacia, porque generaria error

class vacia:
    pass