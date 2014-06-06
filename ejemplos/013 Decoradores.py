#encoding: utf-8

# ******************************************************************************* #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# ******************************************************************************* #


'''
*********************************************************************************
** DECORADORES.                                                      **
** Un decorador no es más que una función que recibe otra función y que devuel-**
** ve otra función ya decorada                                                 **         
*********************************************************************************
'''

def decorador(laFuncion):
	def funcionDecorada(*args, **kwargs): # *args son los argumentos, **kwargs es el diccionario con los argumentos
		print 'Función ejecutada: ', laFuncion.__name__ # laFuncion.__name__ me devuelve el nombre de la función que he enviado a la función decorador
		laFuncion(*args, **kwargs)

	return funcionDecorada

def resta(n, m):
	print n-m

#Decorando
decorador(resta)(5, 3)

# Puedo guardar la función dentro de una variable y puedo usarla siempre
decorada = decorador(resta)

decorada(3, 5)

'''
*********************************************************************************
** Pero python para los decoradores creó el signo @                            **
** Esto nos ayuda a no tener que llamar a decorador pasándole la función       **
*********************************************************************************
'''
def decorandose(laFuncion):
	def funcionDecorada(*args, **kwargs):
		print 'Función ejecutada: ', laFuncion.__name__ # laFuncion.__name__ me devuelve el nombre de la función que he enviado a la función decorador
		laFuncion(*args, **kwargs)

	return funcionDecorada

@decorandose #Le estamos diciendo a python que la función resta es parte de la funcion decorandose que es un decorador
def restita(n, m):
	print n-m

# Cuando yo llame a resta en realidad estamos ejecutando
# decorandose(resta)(5, 3)
restita(5, 3)


# Otro decorador ... ejemplo con decoradores anidados
loggeado = True
usuario = 'CodigoFacilito'

def admin(f):
	def comprobar(*xargs, **xkwargs):
		if loggeado:
			f(*xargs, **xkwargs)
		else:
			print 'No tiene permisos de ejecutar', f.__name__
	return comprobar

def el_decorado(mi_funcion):
	def funcion_el_decorado(*xargs, **xkwargs):
		print "Funcion ejecutandose: ", mi_funcion.__name__
		mi_funcion(*xargs, **xkwargs)

	return funcion_el_decorado

# De esta manera anidandolas, sólo se ejecutará restandose con el decorador el_decorado
# si el decorador @admin lo permite. Por lo que la función se va pasando de un decorador
# a otro decorador hasta ejecutarse. Pero siempre el primer decorador es el último en
# ejecutarse
@admin
@el_decorado
def restandose(n, m):
	print n - m

print 
print
restandose(3, 8)

# Tenemos que tener en cuenta que la funcion ya devolvía un print
# Si lo que queremos es que devuelva el valor lo cambiaríamos por esto

def mi_decorador(funct):
	def laFuncionDe_mi_decorador(*x, **y):
		return funct(*x, **y) #Esto es porque devuelvo valor

	return laFuncionDe_mi_decorador

@mi_decorador
def suma(n, m):
	return n+m

print
print suma(8, 8)
