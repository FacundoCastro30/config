#un iterador es un elemento que contiene un numero contable de valores y puede ser iterado, o sea que se puede pasar por sus variables

#tecnicamente es un bjeto que implementa un protocolo iterador, que consiste de los metodos __iter__() y __next__()

#las colecciones son iterables, o sea que tienen iteradores en si mismas. todos losobjetos de las colecciones tienen el metodo iter() que se usa para obtener un iterador

frutas = ("manzana", "banana", "pera")
miit = iter(frutas)

print(next(miit))
print(next(miit))
print(next(miit))

#la misma logica se puede aplicar a strings

x = "Facundo"
letras = iter(x)

print(next(letras))
print(next(letras))
print(next(letras))
print(next(letras))
print(next(letras))
print(next(letras))
print(next(letras))

#se le puede aplicar for tanto a colecciones como strings

for l in frutas:
    print(l)

for y in x:
    print(y)

#basicamente el for crea un iterator y le aplica next en cada ciclo

#para crear un iterador se implementan __iter__() y __next__()  
# __iter__() se usa similar al __init__() pero siempre debe devolver el iterador en si
#__next__() debe devolver el iterador siguiente de la secuencia. puede realizar operaciones dentro de si

class numeros:
    def __iter__(self):
        self.n = 1       #podria decirse qeu este es el inicio de la serie
        return self
    def __next__(self):
        x = self.n       
        self.n +=1      #y este seria el incremento
        return x

mi_clase = numeros()
mi_iter = iter(mi_clase)

print(next(mi_iter))
print(next(mi_iter))
print(next(mi_iter))
print(next(mi_iter))
print(next(mi_iter))

#si el ejemplo anterior tuviera un ciclo for continuaria por siempre. StopIteration se usa en ese caso para que no ocurra

#se usa en el __next__(), para qeu genere un error al alcanzar un numero definido de iteraciones

class num:
    def __iter__(self):
        self.m = 2
        return self
    def __next__(self):
        if self.m <= 20:
            y = self.m
            self.m +=2
            return y
        else:
            raise StopIteration
        
miclas = num()
miter = iter(miclas)
for z in miter:
    print(z)