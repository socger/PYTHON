#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# DICCIONARIOS, Van predecidas de una clave ... matrices asociativas
# Para leer un elemento tengo que hacer uso de la clave
# *********************************************************************************** #
d = { 'Clave1': [1,2,3],
      'Clave2': True }

# para acceder a uno de los elementos ... elemento nUmero dos .. uso la clave
# Hay que respetar las mayusculas y las minUsculas
print d['Clave2']

e = { 4: 'dedo',
      1: [1,2,3] }

print e[4]

# En los diccionarios se pueden modificar los valores, pero no las claves
e[4] = False
print e[4]
print

# *********************************************************************************** #
# DICCIONARIOS ... ACCIONES O METODOS ... Y ATRIBUTOS
# *********************************************************************************** #

# Para saber si una clave está dentro de un diccionario se usa el método has_key()
diccionario = {
	"redes_sociales": ['Twitter', 'Facebook', 'LinkedIn'],
	3: 'Tres',
	'Hola': "Mundo"
}

print 'Existe la clave dentro del diccionario: ' , diccionario.has_key('Hola')

# Imaginemos que queremos saber todos los pares clave mas valor que existan en un 
# diccionario ... para ello esta el método items(), este método nos devuelve una lista
# conteniendo en cada elemento una tupla donde el primer elemento es la clave y el segundo el valor
print diccionario.items() # Nos devuelve una tupla con el contenido 
                          # [(3, 'Tres'), ('Hola', 'Mundo'), ('redes_sociales', ['Twitter', 'Facebook', 'LinkedIn'])]

# Si solo queremos saber las claves del diccionario ... el método keys()
print diccionario.keys() # Esto nos devolvería una lista con tantos elementos como claves tuviera el diccionario
                         # [3, 'Hola', 'redes_sociales'] 
                         # Es curioso que nos devuelve los valores ordenados por la clave

# Si solo queremos saber los valores del diccionario ... el método values()
print diccionario.values() # Esto nos devolvería una lista con tantos elementos como valores tuviera el diccionario
                           # ['Tres', 'Mundo', ['Twitter', 'Facebook', 'LinkedIn']]
                           # Es curioso que nos devuelve los valores ordenados por la clave

# Para borrar claves y su valor se usa el método .pop()
# Su síntaxis es .pop(valor, d) ... el segundo parámetro es opcional

print
print diccionario
diccionario.pop(3)
#diccionario.pop(4) # Esto nos devolvería un error porque no existe la clave 4
print 'jero que es esto'
print diccionario.pop(4, -1) # Ahora no nos devuelve error porque le decimos que si la clave
                       # no existe que nos devuelva -1 

print diccionario

# Ahora si yo solo quiero borrar un elemento de mi diccionario usaría
# del diccionario[clave]
print
del diccionario['Hola']
print diccionario
print

print 'voy por aqui'
print

# Para borrar todos los elementos de un diccionario (no el diccionario)
diccionario.clear()
print diccionario # Nos devuelve {} porque el diccionario sigue existiendo

# Para agregar valores al diccionario
diccionario["clve"] = "valor"
print diccionario
print

# Se pueden hacer copias de un diccionario en otro diccionario
diccionario_2 = duccionario.copy()
