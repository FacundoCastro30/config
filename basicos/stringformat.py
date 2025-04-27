#desde 3.6 existe el fstring, que ya lo vengo usando en los apuntes
#previo a eso se realizaba mediante format()

x = f"el precio es 50 pesos"
print(x)

#con {} se pueden combinar formats con variables, operaciones, funcines o modificadores

p = 40
txt = f"el precio es {p} pesos"
print(txt)

#con : se pueden agregar modificadores

tex = f"elprecio es {p:.2f} pesos" #.2f es dos decimales 
print(tex)

#tambien se puede hacer directo sobre valores

txto = f"el precio es {80:.2f} pesos"
print(txto)

#admite operaciones
t = f"el precio es {30+30} pesos"
print(t)

#y tambien admite operaciones con variables
price = 100
iva = 0.21
total = f"el precio con impuesto es {price + price*iva:.2f} pesos"
print(total)

#tambien admite if/else
costo = 200
print(f"el producto es {'barato' if costo < 150 else 'caro'}")

#permite utilizar funcoines/metodos

fruta = "manzana"
z = f"yo como {fruta.upper()}"
print(z)

#tambien con funciones custom

def perimetro(x):
    return x * 3.14

peri = f"el area del circulo es de {perimetro(20):.2f} cm"
print(peri)

#otros modificadores so npor ejemplo, separador de miles

miles = 2496872
print(f"numero {miles:,}") #usa coma com oseparador de miles, cada 3 cifras

#la lista de modificadores esta en w3s, incluyen manejos de espacio, simbolos positivos y negativos, "traduccion" a octal, cientifico, binario, etc

#previo a 3.6 se usaba asi:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#txt = "The price is {:.2f} dollars" para dos decimales

#asi con varias variables
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#se pueden aplicar indices para que las variables se usen en el lugar correcto

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#o para repetirlas
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#tambien se pueden nombrar los indices 
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#todos los ejemplos con format() siguen funcionando, pero el metodo preferido es f"