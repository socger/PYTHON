#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# LISTAS, arrays .. en el ejemplo de abajo metemos sobre l, incluso hasta otra lista
# *********************************************************************************** #
l = [2, "tres", True, ["uno", 10]]
print l
#Como acceder a cada uno de los elementos de l
l2 = l[0]
print l2
l2 = l[1]
print l2
l2 = l[2]
print l2
l2 = l[3]
l3 = l2[1]

l4 = l[3][0]
print l2, l3, l4

#Si quiero cambiar uno de los valores de la lista, 
#incluso cambiandole el TIPO
print ""
print l
l[1] = 'cuatro'
l[1] = False
print l

#Puedo tambien crear una lista sacando datos de otra lista
print ""
print l
l2 = l[0:3] #Le digo que coja desde el indice 0, 3 valores
print l2
l2 = l[0:3:2] #eL PRIMER PARAMETRO ES EL INDICE DE DONDE EMPIEZA
			  #eL SEGUNDO PARAMETRO ES LA CANTIDAD DE CAMPOS A TRAER
			  # EL TERCERO ES LA CANTIDAD DE SALTOS A REALIZAR 
			  # POR LO QUE PONDRA EL PRIMERO, SOLO COJERA 3 CAMPOS, PERO EL SEGUNDO NO POR TENER UN SALTO DE CADA DOS
print l2
l2 = l[0::2] #Le digo que coja desde el Indice 0, 3 valores
print l2

#cAMBIAR VALORES A VARIOS CAMPOS DE UNA LISTA
print ""
print l
l[0:2] = [True, False]
print l
l[0:2] = [1] #quito dos valores y los convierto en uno
print l

#Pero tambien podemos acceder a los valores de una lista al reves
print ""
l2 = l[-1] #Coge el ultimo valor de la derecha de la lista
print l2
l2 = l[-2] #Coge el segundo valor de la derecha de la lista
print l2

# Buscar si un elemento está en una lista
lista = [1, "dos", 3]
buscar = 1

print buscar in lista # si el contenido de buscar esta en lista me devuelve True, si no False

# *********************************************************************************** #
# LISTAS ... ACCIONES O METODOS ... Y ATRIBUTOS
# *********************************************************************************** #
# ¿Como buscar el índice de un elemento dentro de una lista?
print lista.index(buscar) # Me devuelve el índice si existe el elemento que hay dentro de buscar en 
                    # lista, por lo que me devolverá un 0 (posición primera)

if buscar in lista:
	print lista.index(buscar)
else:
	print "No existe el elemento dentro de la lista"

# Como añadir elementos a una lista... método append
print
print lista

lista.append("Nuevo elemento")
print lista

# Método para ver cuantas veces aparece un elemento en la lista
print lista.count(3) #Me devolverá un uno, que son las veces que aparece el 3 dentro de la lista

# También tenemos un método para in ertar elementos en cierta posición.
# Su síntaxis sería lista.insert(posición, elemento)
print
print
print
print
print lista
lista.insert(2, "otro elemento")
print lista
print
print

# También podemos unir dos listas, se añadirían los elementos de la segunda al final de la primera
# Su síntaxis sería lista1.extend(lista2), por supuesto lo que se añada puede ser una cadena, una lista o una tupla
cadenilla = "mi cadena"
lista2 = [1,2,3,4]
lista.extend(cadenilla) #Esto lo que hará será añadir a lista tantos elementos como caracteres tuviera cadenilla
print lista
print
print
lista.extend(lista2) # Esto lo que hará será añadir a lista tantos elementos como elementos tuviera lista2
print lista
print
print

# Ahora veamos como buscar un elemento y extraerlo de la lista (quitarlo)
# Su síntaxis sería lista.pop(índice) ... si no le ponemos índice nos saca el último elemento
lista = [1,3,"Dos", 4]
print lista
lista.pop() #Me saca y borra el último elemento de la lista
print lista
lista.pop(1) # Me saca y borra el elemento en la posición uno, o sea el que tiene como contenido un 3
print lista
print
print

# Ahora veamos como buscar un elemento y extraerlo de la lista (quitarlo), 
# pero buscando por el valor del elemento, no por su índice (posición)
lista = [1,3,"Dos", 4, "Dos"]
print lista
lista.remove('Dos') #Esto lo que hace es retirar el elemento cuyo contenido sea 'Dos'
                    #Pero sólo quitaría el primer elemento más a la izquierda
print lista
print
print

# Cómo cambiar el orden de la lista, es decir cómo si la lista es 1,2,3 como convertirla
# a 3,2,1
lista = [1,2,3]
print lista
lista.reverse() #Obviamente sus índices cambian de valor
print lista
print 
print

'''
*************************************************************************************
COMPRENSION DE LISTAS

Vienen a reemplazar el uso de las funciones map y filter


*************************************************************************************
'''
l1  = [1,2,3,-1,4]
sss = ["H", "O", "L", "A"]

# Las comprensión de listas siempre nos devuelven algo, por lo que num es lo que nos
# devuelve y también el número que recorremos de la lista l1
# Lo que hay desde el <if> es lo que queremos que filtre
l2 = [num for num in l1 if num>0]

# Lo que hacemos es multiplicar el caracter (car) que recogemos de la lista sss
# por el número (num) recogido de la lista l1, pero sólo si el número no es
# negativo
l3 = [car * num
        for car in sss
                for num in l1
                        if num > 0 ]

print
print l1
print l2
print l3

'''
*************************************************************************************
GENERADORES 

Vienen a SER lo que era la comprensión de listas, pero pudiendo recorrer uno a uno
cada elemento

Básicamente en el ejemplo anterior lo que hacemos es sustituir los corchetes por
paréntesis
*************************************************************************************
'''
l1  = [1,2,3,-1,4]
sss = ["H", "O", "L", "A"]

l3 = (car * num
        for car in sss
                for num in l1
                        if num > 0 )

'''
print
print l1
print l3.next() # Cada next() es un elemento del generador
print l3.next()

Pero como no vamos a estar contínuamente poniendo un .next() para cada elemento
sustituiremos esto por un for
'''
print
print

for letra in l3:
        print letra # El for ya hace el .next() él solito

''' Veamos otro ejemplo con el uso de los generadores
    En este caso usaremos una función como objeto generador, por eso usamos ...
    yield '''
print

l = [1,2,3,-1,4]
s = ["H", "O", "L", "A"]

def factorial(n):
        i = 1;
        while n > 1:
                i = n * i
                yield i
                n -=  1 
                
for e in factorial(5):
        print e

''' Contenido sacado de http://pythonmania.wordpress.com/

    Básicamente los generadores se escriben funciones normales, pero usan la
    sentencia yield en vez de un return dentro de un bucle. Yield funciona de
    manera similar al return, pero la gracia de usar el yield es que conserva
    la iteración del bucle para la siguiente vez que se le invoque, esto queda
    mas claro con un ejemplo '''

print

def contador(max):
        n=0
        while n < max:
                yield n
                n +=1


gen = contador(3)

print gen.next()
print gen.next()
print gen.next()

''' Contenido sacado de http://pythonmania.wordpress.com/

    Al invocar el “contador” que definimos, este devuelve un objeto de tipo
    Generator. Este objeto tiene el método next() que permite ir obteniendo
    valores del bucle cuando se necesitan y cuando los generadores terminan su
    ejecución, hacen saltar la excepción StopIteration automáticamente.
    
    Además, podemos hacer varias cosas, como por ejemplo usar el yield dentro
    de un bucle infinito (en el siguiente ejemplo seria el while True) de esta
    manera cuando termina de iterar vuelve a empezar. En este caso voy a hacer
    que recorra los elementos de un lista '''

def recorre(list):
        while True:
                for n in list:
                        yield n

gen = recorre([1, "a", 2, "hola"])

print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()

''' Y podríamos continuar así de manera indefinida (evidentemente la lista
    puede contener cualquier cosa). La utilidad de esto es que se pueden usar
    iterables fuera de un bucle de una manera sencilla. '''

