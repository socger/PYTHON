#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# HERENCIA
# *********************************************************************************** #
class Ingeniero_Sistemas(Persona): # Le estamos diciendo que la clase Ingeniero_Sistemas heredan de la clase Persona
	def programar(self, lenguaje):
		print 'Voy a programar en ', lenguaje

class Licenciado_Derecho(Persona):
	def __init__(self):
		print 'HOLITA'

	def estudiarCaso(self, de):
		print 'Debo estudiar el caso de ', de

# La clase Ingeniero _Sistemasno tiene el método init (constructor) porque lo 
# heredan de la clase Persona, así que cuando instanciamos un objeto de la 
# clase Ingeniero_Sistemas, en realidad arrancamos con el init de la 
# clase Persona

# La clase Licenciado_Derecho, le hemos creado un constructor para que pase del
# constructor de la clase que hereda (Persona). Por eso no le paso parámetros 
# cuando creo el objeto de ella (Miriam)


Mari = Ingeniero_Sistemas(16)
Miriam = Licenciado_Derecho()

# Por lo que también podemos hacer llamadas a atributos o métodos 
# de la clase Persona
print Mari.dime_edad('Mari tiene ')

# Y por supuesto podemos hacer llamadas a atributos o métodos
# propios de esta clase, no de la que hereda
Mari.programar('python')
Miriam.estudiarCaso('los córdoba')

print


# *********************************************************************************** #
# HERENCIA MULTIPLE
# *********************************************************************************** #
class Estudioso(Ingeniero_Sistemas, Licenciado_Derecho):
	pass #Se podría interpretar como un VETE (no hay nada aqui)

# Una clase tiene que tener como minimo algo (atributos, metodos) al declararla
# Si no tiene nada pues ponemos PASS para no haga nada pero se cree bien

# La clase estudioso hereda de las clases Ingeniero_Sistemas y Licenciado_Derecho, y como 
# estas heredan de la clase Persona, pues la clase estudioso también heredara de la clse 
# Persona. 

# Pero hay que tener en cuenta un problema, la clase Persona tiene un 
# constructor pero la clase Ingeniero_Sistemas, no lo tiene. Mientras 
# que la clase Licenciado_Derecho si que lo tiene. Entonces hay que 
# tener en cuenta que tiene preferencia el método init de la clase 
# persona. Pero si la creación de la clase estudioso fuera así
# class Estudioso(Licenciado_Derecho, Ingeniero_Sistemas):
# entonces el método init (constructor) tendría preferencia el de
# la clase Licenciado_Derecho

# Ahora imagimenos que todas tuvieran un constructor, entonces se 
# tomaria el constructor de la clase heredada mas a la izquierda
# En el caso class Estudioso(Ingeniero_Sistemas, Licenciado_Derecho):
# tomaría el constructor de la clase Ingeniero_Sistemas

pepe = Estudioso(15)

# Así podemos usar métodos, atributos del objeto pepe, aunque sean de 
# diferentes clases
pepe.programar('C++')
pepe.estudiarCaso('de sus hijos')
print pepe.dime_edad('Pepe tiene ')
print
