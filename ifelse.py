#if... else

#es un condicional como en JS
#comparaciones

"""
igual ==
diferente !=
mayor >
menor <
mayor o igual >=
menor o igual <=
"""

#fundamental la indentacion

a = 1
b = 545
c = 19
if a == b:
    print("hola")

#elif puede usarse como siguiente condicion

#else se usa como ultima condicion, si no se cumple ninguna otra

if a > c:
    print("chau")
elif a == c:
    print("que tal")
else:
    print("deberia printear esto")

#ternario o short hand: se puede hacer en una linea. caso solo if:

if b == c: print("Facundo")

#caso if, else

print("A") if b > c else print("jaja")

#caso con varias condiciones:

print("A") if a > b else print("=") if a == b else print ("B")

#keywords logicos and, or y not
#and se usa para hacer cumplir ambas condiciones, or para al menos una, y not para invertir el resultado

d = 10
e = 15
f = 20

if d < e and d < f:
    print("ambas se cumplen")

if d > e or d < f:
    print("al menos una se cumple") #si se cumplen ambas sirve igual

if not e == f:
    print("no se cumple")

#se pueden anidar ifs

num = 11

if num > 5:
    print("mayor que 5, ")
    if num > 10:
        print("y que 10")
    else: 
        print("pero no que 10")

#los ifs no pueden estar vacios. en caso de necesitarlo, para no generar error se usa la palabra clave pass

if num < 100:
    pass



