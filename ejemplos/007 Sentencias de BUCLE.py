#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# BUCLES
# *********************************************************************************** #
edad = 0

# Al igual que con los if la tabulación hace saber que las lineas siguientes con la misma
# tabulacíón son del cumplimiento del while
while edad <= 20:
	if edad == 15:
		edad =  edad + 1
		continue # Con esta sentencia no hace caso a las líneas siguientes y sigue con el bucle

	if edad == 19:
		break # Con esta sentencia no hace caso a las líneas siguientes y sale del bucle

	print 'Tienes: ' + str(edad) # La funcion str convierte la variable edad en string
	edad = edad + 1


# Ahora el bucle for
print

lista = ['Elemento 1', 'Elemento 2', 'Elemento 3']	

#cosa irá recogiendo cada uno de los valores de lista
for cosa in lista:
	print cosa

# podemos recorrer también cada uno de los caracteres de una cadena
for letra in 'Mi casa es demasiado chica':
	print letra

