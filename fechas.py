#python no tiene un tipo de fecha como dato, pero se puede usar el modulo datetime 

import datetime

x = datetime.datetime.now()
print(x)

#la info vien en formato año, mes, dia, hora, min, seg y microseg

#tiene varios metodos, depende de la informacion que se necesite. ejemplos

print(x.year)
print(x.strftime("%d")) #%d es dia del mes

#datetime tambien se puede usar como constructor para crear objetos de fecha

y = datetime.datetime(1989, 1, 30) #default es año, mes, dia
print(y)

#parametros opcionales: h,m,s,ms (0 por defalut), zona horaria (none por default)

#el metodo strftime() se usa para hacer mas legible la data. recibe un parametro llamado format, usado para pedir algo especifico (la lista esta en w3s)

print("tu dia de nacimiento fue un " + y.strftime("%A"))