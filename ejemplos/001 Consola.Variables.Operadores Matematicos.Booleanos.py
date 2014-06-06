#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# Como presentar por la consola algo
# *********************************************************************************** #
print ("Hola ñññ Python")
print ("Hola Python")
print "Hola Python", "solo para versiones anteriores a la 3.0 de python" 
print "Hola Python"
print ("Hola Python")

# *********************************************************************************** #
# Jugando con variables
# *********************************************************************************** #
e=5 #int
e=5L #long int
e=12.07 #float

a = 26
b = 11.35
c = 5
d = 3.5

# *********************************************************************************** #
#LA FUNCION type() NOS DEVUELVE EL TIPO DE VARIABLE QUE ES
# *********************************************************************************** #
print type(b)

# *********************************************************************************** #
# OPERADORES MATEMATICOS
# *********************************************************************************** #
# suma
print a + b

#resta 
print c -a

# Multiplicacion
print d*c

# Exponente .. elevar
print c ** 2

# Division, tengo que convertir la variable c a float 
# porque si no la division me devuelve un numero entero
print float(c) /a

# Division entera ... sin decimales
# esta division nos deberia de devolver 2.33333333 en una calculadora, pero sin embargo nos devuelve 2
print 7 / 3

# Modulo ... Nos devuelve le resto de una division
print 7%3

# *********************************************************************************** #
# BOOLEANOS ... importante poner True o False, no true / false
# el editor no lo reconoceria
# *********************************************************************************** #
bT = True
bF = False

# Operadores and or y not
bAnd = bT and bF #Devuelve false porque los dos no son True
bOr = bT or bF   #Devuelve True porque alguno de los dos es true
bNot = not bF    #Devuelve True porque pone lo contrario al valor de bF(False)

print bAnd, bOr, bNot

