#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# OPERADORES RELACIONALES
# *********************************************************************************** #
v = 3
c = 5

# comparamos c con v y si son diferentes devuelve false, si son iguales devuelve true
r = c == v
print r

v = 5
c = 5

r = c == v
print r

# El inverso es != .. diferente de.. por lo que si son diferentes
# devuelve true y si son iguales devuelve false

v = 4
c = 5

r = c != v
print r

# Para saber si un valor es mayor o menor que otro elemento, devuelven
# false si no se cumple y true si se cumple
r = c > v
print r

r = c < v
print r

# tambien se pueden hacer comprobaciones de mayor o igual, y de 
# menor o igual
r = c >= v
print r

# Tambien se pueden usar con las cadenas
# Y en general con listas, tulipas y diccionarios tambien
v = 'Hola'
c = 'Adios'

r = c == v
print r

# *********************************************************************************** #
# SETENCIAS CONDICIONALES
# *********************************************************************************** #
edad = 16
mayoria_edad = 18

# Importante, las setencias que cumplen la condicion if tienen una tabulacion
# Si se quita la tabulacion python cree que no pertenecen al if
if edad >= mayoria_edad:
	print "Eres mayor de edad"
	if True:
		print 'Esto se ejecuta siempre que sea mayor de edad'
	else: #Este es el else del segundo if
		print "no pasa nunca por aqui"
else: # Este es el else del primer if y lo marca su tabulacion
	print 'No eres mayor de edad'

# El segundo if esta dentro de las lineas a ejecutarse si se cumple el
# primer if. Esto lo marca la tabulacion

print "Esto se ejecuta siempre"

# Otro ejemplo de if y else if (elif)
print

edad = 78
if edad >= 0 and edad < 18:
	print 'Eres un niño'
elif edad >= 18 and edad < 27:
	print 'Eres un joven'
elif edad >= 27 and edad < 60:
	print 'Eres un adulto'
else:
	print 'Eres de la tercera edad'

# *********************************************************************************** #
# SETENCIAS switch ... nO EXISTE EN python
# *********************************************************************************** #

