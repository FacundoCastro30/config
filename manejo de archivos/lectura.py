#si tenemos un archivo dentro de la misma carpeta, podemos abrirlo con open(). esto devuelve un objeto que tiene un metodo read()

a = open("prueba.txt")
print(a.read()) #muestra el contenido del archivo

#se puede aclarar la ruta para trabajar con archivos en otras carpetas

b = open(r"C:\Users\Facundo (Laboral)\Desktop\escritorio.txt")
print(b.read())

#tambien se puede usar el statement with

with open("prueba.txt") as c:
    print(c.read())

#with se encarga de cerrar el archivo. es buena practica cerrarlos, por temas de buffer y porque archivos modificados no muestran cambios hasta cerrarse. sino se usa el with, hay que cerrarlo a mano:

d = open("prueba.txt")
print(d.readline(2))
d.close()

#el metodo read() admite como parametro un numero con cuantos carcteres qeuremos que nos devuelva. pordefault es todo el archivo

#el metodo readline() nos lee renglon por renglon

e = open("prueba.txt")
print(e.readline())
print(e.readline())
e.close()

#tambien se puede loopear

with open("prueba.txt") as f:
    for x in f:
        print(x) #donde x es cada renglon, incluso los renglones en blanco