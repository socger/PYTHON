#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# TUPLAS
# *********************************************************************************** #
t = 1, True, "Hola"
print t # El problema es que pone los parentesis aunque no los tuviera

# Asi que el modo correcto es con parentesis
t = (3, "hola", False)
print t
print type(t)

# Acceder a un elemento de la tupla
# En principio es aplicable todo lo de las listas, pero las tuplas
# se diferencian de las listas en que a las tuplas son fijas. Si se 
# crean con 3 elmentos no se le pueden anadir mas, mientras que a 
# las listas si. Ademas las tuplas sus elementos no pueden ser modi-
# ficados una vez creados

print t[2]

