#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# CADENAS 
# *********************************************************************************** #
cads = 'con comillas simples'
cadd = "con comillas dobles"
cd = type (cads)
print cd

# caracteres escape \n .. deja una linea (salto de carro)
#                   \t ... hace el efecto del tabulador
cadd = "con comillas \n\tdobles"
print cadd

# Si deseamos crear parrafos de texto
print ""
cadena = """Texto linea 1
Linea 2
Linea 3
.
.
.
.
Linea N
"""
print cadena
print ""

# Tambien nos permite hacer repeticiones sobre string
cadena = cadena * 3
print cadena

# Concatenar string
cadena1 = "hola"
cadena2 = "Jero"
cadena3 = cadena2 + ", " + cadena1
print cadena3

# *********************************************************************************** #
# CADENAS ... ACCIONES O METODOS ... Y ATRIBUTOS
# *********************************************************************************** #
print len(cadena3) # La función len nos devuelve la longitud de la cadena en caracteres

# Ahora veremos como contar la cantidad de veces que se repite un literal en una cadena
# La sintaxis seria ... cadena.count(valor, inicio, fin)
print cadena3.count('hola', 0, len(cadena3)) # Cuantas veces se repite el literal "hola" 
                                             # dentro de cadena3, desde su inicio(0), y hasta 
                                             # el total de la longitud de cadena3

print cadena3.count('o') # El inicio y el final son opcionales, así buscaría el literal "o" 
                         # en toda la longitud de cadena3.

print cadena3.count('P', 0, 4) # Tenemos que tener en cuenta que la posición de inicio es el 0
                               # y que la posición hasta la que queremos comprobar es la 4, por
                               # lo que en realidad comprobará en los 5 primeros caracteres de 
                               # cadena3   
                               # Es digno de mencionar que hace diferencia entre minúsculas y 
                               # mayúsculas

print cadena3.count('o', 5) # Al no poner uno de los parámetros, considera el segundo como el 
                            # el inicio de la búsqueda. Y por lo tanto buscará el literal "o"
                            # dentro de cadena3 desde la posición 5(caracter 6) y hasta el 
                            # último caracter de cadena3

# Ahora veamos como convertir una cadena en minúsculas o mayúsculas toda ella
print cadena3.upper() # Nos devuelve cadena3(su contenido) todo en mayúsculas
print cadena3.lower() # Nos devuelve cadena3(su contenido) todo en minúsculas

# Ahora vamos a ver como sustituir un literal por otro literal dentro de una cadena
# Su síntaxis sería CADENA.replace(valor, nuevo, repeticiones)
# Los dos primeros parámetros son obligatorios, el tercero es opcional
print cadena3.replace('o', 'x') # Esto reemplazaría todas las "o" de cadena3 por "x"

print cadena3.replace('o', 'x', 3) # Esto reemplazaría la "o" de cadena3 por "x", pero sólo 
                                   # unas 3 veces. Si hubieran más de 3 "o", sólo reemplazaría
                                   # las tres primeras

# Veamos como dividir una cadena por un literal en concreto
# Su síntaxis sería CADENA.split(separador, maxsplit)                                   
vari = 'Hola mundo'
print vari.split("a") # Esto nos devuelve una lista de la siguiente forma
                      # ['Hol', ' Mundo']

print vari.split('o') # Esto nos devuelve una lista de la siguiente forma
                      # ['H', 'la Mund, ''] .. 3 elementos ahora

print vari.split('o', 1) # De esta manera nos lo va a cortar sólo una vez
					     # donde aparezca la pimera o

print vari.split() # De esta manera nos la va a cortar la cadena por el primer espacio en blanco
				   # Devuelve ... ['Hola', ' Mundo']

print vari.split(' ') # De esta manera nos la va a cortar la cadena por el primer espacio en blanco
				      # Devuelve ... ['Hola', ' Mundo']

# Veamos ahora como encontrar una cadena dentro de otra cadena.
# Su síntaxis sería CADENA.find(valor, inicio, fin)							
print vari.find('a') # Esto nos devolvería un 3 ... posición donde se encuentra la primera letra a 
                     # Hay que tener en cuenta que la posición 0 es la letra H

print vari.rfind('o') # Esto nos devolvería un 9 porque busca la primera letra o, pero empezando a 
                      # buscarla desde la derecha, pero evidentemente contando con que la posición 0 
                      # sigue siendo la primera letra de la izquierda

# JOIN.. nos devuelve una cadena de una tupla o una lista, pero separados por un caracter, su uso 
# podría ser interesante para hacer exportaciones a format CSV, etc
# Síntaxis CADENAS.join(secuencia)
t = ("H", "o", "l", "a")
cadenita = ";"

print cadenita.join(t) # Como cadenita tenía dentro el caracter ; ... ahora la variable cadenita 
                       # contendrá todos los elementos de la tupla t, separados por el caracter ;
                       

print
print
print

print 'jolin'

