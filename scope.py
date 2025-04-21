#el scope es similar a otros lenguajes. una variable solo existe en el entorno en el que se la define. una variable dentro de una funcion solo existe dentro deesa funcion, una variable declarada fuera detoda funcion se puede usar en cualquier momento

#scope local: una vari(able declarada en una funcion esta disponibke dentro de la misma y en las funciones que se encuentren dentro de ella

def f1():
    x = 10
    def f2():
        print(f"funcion interna {x}")
    f2()

f1()

#scope global: una variable declarada en el cuerpo del script es accesible para cualquire funcion

y = 20

def f3():
    print(y)

f3()
print(f"{y} pero desde un print directo")

#considerendo el scope, dos variables pueden llamarse igual pero ser distintas si son de distinto scope

z = 30

def f4():
    z = 40
    print(f"z local: {z}")


print(f"z global: {z}")
f4()

#la palabra clave global hace que una variable de scope local sea global


def varglob():
    global var
    var = "Facundo"
    print(f"desde funcion: {var}")

varglob()
print(f"desde print: {var}")    


#usando global tambien podemos darle nuevo valor a una variable global dentro de una funcion

q = 43

def f5():
    global q
    q = 50
    print(q)

f5()


#la palabra clave nonlocal hace que una variable de una funcion anidada pase al scope de la funcion padre, pero no al scope global


def f6():
    w = "hola"
    def f7():
        nonlocal w
        w = "chau"
    f7()
    return w

print(f6())