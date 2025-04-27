#los metodos write "w" y append "a" del open(), se usan para escribir. append agrega al final, write sobreescribe

with open ("prueba.txt", "a") as a:
    a.write(" \nse agrego esta linea")

with open("prueba.txt") as a:
    print(a.read())

#haciendo el mismo open() pero con parametro "w" se sobreescribe todo el archivo, no voy a probarlo 

#para crear, metodo open() y "x"

with open("prueba2.txt", "x") as b:
    b.write("hola, soy un archivo nuevo")