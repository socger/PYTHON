#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# FUNCIONES
# *********************************************************************************** #
# Tambien es necesario la tabulacion
#Los parametros tambien los puedo inicializar, por si se llama a esta funcion sin pasarle parametros
def mi_funcion(num1=0, num2=0): 
	print
	print num1 + num2

def mi_funcion_2(cadena, veces=2): 
	cantidad = 1
	variable = ''

	print
	while cantidad <= veces:
		variable = variable + cadena
		cantidad = cantidad + 1

	print variable

	# todo lo anterior se hubiera solucionado con simplemente la linea siguiente
	print cadena * veces
	
def mi_funcion_3(cadena, veces=2, *algomas): 
	# Todo parámetro que vaya después de los dos primeros se guardarán en una tupla
	# Pero tengo que ponerle un * antes del nombre del parametro	
	print
	print cadena * veces

	# Recorremos la tupla
	for cadena in algomas:
		print cadena * veces
	
def mi_funcion_4(cadena, veces=2, **algomas): 
	# Todo parámetro que vaya después de los dos primeros se guardarán en un diccionario
	# Pero tengo que ponerle dos * antes del nombre del parametro	
	print
	print cadena * veces

	print algomas['cadenaextra']
	print algomas['cadenademas']

def devolver_suma(num1=0, num2=0):
	return num1 + num2

mi_funcion(3, 4)
mi_funcion()

mi_funcion_2('La ', 3)
mi_funcion_2('La ')

mi_funcion_3('La ', 3, 'Hola', 'Adios', 'otra cadena', 'para que veas que funciona')
mi_funcion_4( 'Phyton ', 5, cadenaextra = 'Hola', cadenademas = 'adios' )

print 
print devolver_suma(8, 4)

resultado = devolver_suma(8, 4)
print resultado

# *********************************************************************************** #
# FUNCIONES DE ORDEN SUPERIOR
# *********************************************************************************** #
# En python podemos crear dos funciones y una que al llamarla le pase como parámetros
# otra funcion
# *********************************************************************************** #
def prueba(funcion):
        return funcion() # lo que hacemos es llamar a la funcion para que devuelva algo

def porEnviar():
        return 2+2

# Como verás se llama a la funcion prueba y se le pasa entre paréntesis la otra función
# y no hace falta hacer esto ... prueba(porEnviar())
print
print
print prueba(porEnviar)

'''
*************************************************************************************
Podemos crear funciones dentro de otras funciones, es decir funciones que reciben
como parámetros otras fuciones

La funcion seleccion recibe sólo un parámetro(opracion), pero dentro tiene otras dos
funciones (suma y multiplicacion), pero estas tienen dos parametros (n,m)
*************************************************************************************
'''

def seleccion(operacion):
        def suma(n,m):
                return n + m
        
        def multiplicacion(n,m):
                return n * m
                
        if operacion == "suma":
                return suma # aqui lo que devolvemos en realidad no es el valor de la funcion suma .. no .. lo que devolvemos es en si la funcion
        elif operacion == "nulti":
                return multiplicacion # aqui lo que devolvemos en realidad no es el valor de la funcion suma .. no .. lo que devolvemos es en si la funcion

fGuardada = seleccion("suma") # asi que fGuardada se convierte en realidad en una funcion por lo que podemos llamarla pasandole parámetros
print
print fGuardada(3,4) # llamamos a una funcion que creamos en tiempo real y que es igual a la funcion que nos devuelve (return) seleccion

'''
*************************************************************************************
Básicamente lo anterior sirve para ver cual es la diferencia entre llamar a una
funcion para que nos devuelva un cálculo ... que se haría llamando a la funcion con
sus paréntesis

O llamar a la función para que nos devuelva una función que es sin ponerle los
*************************************************************************************
'''


'''
*************************************************************************************
Bien ahora vamos a trabajar con la funcion de orden superior MAP
*************************************************************************************
'''

def operador(n, m):
        # Con este if de abajo controlamos cuando le falta uno de los parámetros(None que es un campo null)
        # Así controlamos el error de que no se pueden sumar enteros con campos nulos
        if n==None or m ==None:
                return 0
        
        return n+m

Lista1 = [1, 2, 3, 4]
Tupla1 = (9, 8, 7, 6)

lr = map(operador, Lista1, Tupla1) # la función map le envía a la funcion operador los
                                   # elementos Lista1 y Tupla1 como si fueran parámetros
                                   # por lo que la funcion operador recibe en n y m
                                   # (parámetros) la lista y la tupla

print
print Lista1
print Tupla1
print lr

# Pero que pasaría si por ejemplo la tupla tuviera un número menos

Lista1 = [1, 2, 3, 4]
Tupla1 = (9, 8, 7)
lr = map(operador, Lista1, Tupla1) # la función map le envía a la funcion operador los
                                   # elementos Lista1 y Tupla1 como si fueran parámetros
                                   # por lo que la funcion operador recibe en n y m
                                   # (parámetros) la lista y la tupla

print
print Lista1
print Tupla1
print lr

# También podemos usar map para cadenas
s1 = 'Hola'
s2 = 'mundo'

print
print map(operador, s1, s2) # Esto me va a devolver ... ['Hm', 'ou', 'ln', 'ad', 0]

'''
*************************************************************************************
map(function, sequence[, sequence, ...])

La función map aplica una función a cada elemento de una secuencia y devuelve una
lista con el resultado de aplicar la función a cada elemento. Si se pasan como
parámetros n secuencias, la función tendrá que aceptar n argumentos. Si alguna de las
secuencias es más pequeña que las demás, el valor que le llega a la función function
para posiciones mayores que el tamaño de dicha secuencia será None.

A continuación podemos ver un ejemplo en el que se utiliza map para elevar al
cuadrado todos los elementos de una lista:
*************************************************************************************
'''
def cuadrado(n):
    return n ** 2

l = [1, 2, 3]
l2 = map(cuadrado, l)
print
print l
print l2

'''
*************************************************************************************
Bien ahora vamos a trabajar con la funcion de orden superior FILTER

Va recibir una función y va a recibir sólo una lista. Va iterar sobre cada uno de los
elementos de la lista

El va a filtrar los valores de la lista y nos devolverá otra lista con los valores
que devuelva un filtro (true), según los valores que definamos en la función
*************************************************************************************
'''

def filtro(elementos):
        return (elementos > 0) # Esta es la condición que tendrá para devolverme los
                               # valores que la cumplan


Lista = [1, -3, 2, -7, -8, -9, 10]

print
print Lista
print 'De la lista anterior, sólo son positivos: ', filter(filtro, Lista)

# Otro ejemplo
def filtro(elementos):
        return (elementos == 'o') # Esta es la condición que tendrá para devolverme los
                               # valores que la cumplan
s = "Hola mundo"

print
print s
print 'De la cadena anterior la cantidad de letras 0 son = ', filter(filtro, s)

'''
*************************************************************************************
filter(function, sequence)

La funcion filter verifica que los elementos de una secuencia cumplan una determinada 
condición, devolviendo una secuencia con los elementos que cumplen esa condición. Es 
decir, para cada elemento de sequence se aplica la función function, si el resultado 
es True se añade a la lista y en caso contrario se descarta.
A continuación podemos ver un ejemplo en el que se utiliza filter para conservar solo 
los números que son pares.
*************************************************************************************
'''

def es_par(n):
	return (n % 2.0 == 0) # Al dividirlo por dos si el resto es 0 es que es
                              # par

l = [1, 2, 3]
l2 = filter(es_par, l)

'''
*************************************************************************************
Bien ahora vamos a trabajar con la funcion de orden superior REDUCE

Esta función nos permite reducir una cadena/lista a ún sólo elemento

reduce(function, sequence[, initial])
La función reduce aplica una función a pares de elementos de una secuencia hasta 
dejarla en un solo valor.
*************************************************************************************
'''
def concatenar(a,b):
	return a+b

tupla_100 = ('H', 'o', 'l', 'a', '_', 'M', 'u', 'n', 'd', 'o')

sr = reduce(concatenar, tupla_100)
print
print type(sr)
print sr


# A continuación podemos ver un ejemplo en el que se utiliza  reduce para sumar todos los elementos de una lista.
def sumar(x, y):
	return x + y
	
l = [1, 2, 3]
l2 = reduce(sumar, l)

print
print type(l2)
print l2

'''
*************************************************************************************
FUNCIONES LAMBDA

El operador lambda sirve para crear funciones anónimas en línea. Al ser funciones
anónimas, es decir, sin nombre, estas no podrán ser referenciadas más tarde.
Las funciones lambda se construyen mediante el operador lambda, los parámetros de la
función separados por comas (atención, SIN paréntesis), dos puntos (:) y el código de
la función.
Esta construcción podrían haber sido de utilidad en los ejemplos anteriores para
reducir código.
*************************************************************************************
'''
li = [1,-2,1,-4]
lo = [5,3,6,7]
s  = "Hola Mundo"

# Ahora guardamos en una variable una función lambda
ss = lambda n,m: n+m

print
print map(ss,li,lo) # Usamos en una función map, una función lambda guardada en una variable (ss)
print filter(lambda n: n=='o', s) # Usamos una función lambda dentro de una funcion filter
print reduce(ss,lo) #Usamos una función lambda guardada dentro de una variable(ss) para una función reduce

print ss(3,4)


