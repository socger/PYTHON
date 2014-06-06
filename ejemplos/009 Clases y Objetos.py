#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


# *********************************************************************************** #
# CLASES Y OBJETOS  .. Atributos y acciones (metodos)
# *********************************************************************************** #

# *********************************************************************************** #
# OBJETOS .. Atributos y acciones (metodos)
# Clases
# *********************************************************************************** #

# todos los nombres de clase empiezan por mayúsculas, aunque no es obligatorio
# también usa la tabulación
# Cada clase tiene que tener un método de inicialización def __init__(self), cada vez 
# que se cree un objeto de la clase ejecutará este método de inicialización.
# Es importante aclarar que la inicialización lleva dos signos __ antes y después de 
# la palabra init ... __init __
# Python también tiene constructor, pero rara vez se usa
# En la variable self se guarda la referencia al objeto
class Humano:
	# Acciones, métodos
	def __init__(self):
		self.edad = 25 # Atributo
		print 'Soy un nuevo objeto'

	def hablar(self, mensaje):
		print mensaje

# Vamos a crear un objeto de la clase humano
pedro = Humano()
raul = Humano()

print
pedro.hablar('Hola') #Si nos damos cuenta no mandamos el parámetro self porque python lo asume por default, pero si hubieran mas parametros son obligatorios ponerlos
raul.hablar('adios')

print
print 'Soy Pedro y tengo ', pedro.edad, ' años'
print

# Ahora veamos como pasarles valores a los atributos
class Persona:
	def __init__ (self, param_edad):
		self.edad = param_edad

	def dime_edad(self, param_msg):
		print param_msg, self.edad


# Fuera de la declaración de la clase
jorge = Persona(25)
jero = Persona(18)

print
print 'Soy Jorge y tengo ', jorge.edad
print 'Soy Jero y tengo ' , jero.edad
print  

print jero.dime_edad('Jero tiene ')
print

# *********************************************************************************** #
# OTRO SUPUESTO DE CLASES Y OBJETOS                                                   #
# *********************************************************************************** #
import math # Importamos la librería en puthon math ... para operaciones matemáticas

class Punto:
	def __init__(self, x = 1, y = 1):
		self.mover(x, y)

	def mover(self, x, y):
		self.x = x
		self.y = y
	def reiniciar(self):
		self.mover(0, 0)
	def calcular_distancia(self, otro_punto):
		# Usamos el teorema de Pitágoras para calcular la distancia entre dos coordenadas x,y
		# Para usamos la raiz cuadrada del cálculo entre paréntesis. No olvidemos que ** es 
		# elevar algo a un exponente. En este caso x**2 es elevar x al cuadrado
		return math.sqrt( 
			( self.x - otro_punto.x ) ** 2 +
			( self.y - otro_punto.y ) ** 2 )

punto1 = Punto()
punto2 = Punto()

punto1.reiniciar()
punto1.mover(4, 8)

punto2.mover(5, 0)

print punto2.calcular_distancia(punto1)

punto3 = Punto() # Cogerá los valores del __init__
punto4 = Punto(4, 5) # Inicializará con los parámetros pasados

print
print punto3.x, punto3.y
print punto4.x, punto4.y

# *********************************************************************************** #
# USO DE DOCSTRINGS ... DOCUMENTACION DE CLASES Y METODOS
# Si usamos bién los docstring, python nos los convierte en documentación de la API
# En el shell del sist.Op pondríamos:
# python -i nombre_apli.py
# Y luego pondríamos help(nombre de la clase)
# *********************************************************************************** #
# REGLAS:
# Cada clase, función o método puede tener un string Python estandard
# Debe ser la primera línea después de la definición
# Debe de estar indentada / sangrada con el resto del código
# Tienen que estar encerrados entre comillas simples o dobles
# Si los comentarios docstrings son muy largos tenemos que formatearlos con unas
# comillas triples, bien simples o dobles.
# *********************************************************************************** #
class Puntito:
	'Representa un punto en coordenadas geométricas bidimensionales'

	def __init__(self, x = 0, y = 0):
		''' Inicializa la posición de un nuevo punto. Las coordenadas x y pueden 
		ser especificadas.. Si no lo son, el punto por defecto será el de origen. '''
		self.mover(x, y)

	def mover(self, x, y):
		"Mueve el punto a una nueva localización en un espacio bidimensional."
		self.x = x
		self.y = y

	def reiniciar(self):
		'Reinicia el punto al origen geométrico: 0, 0'
		self.mover(0, 0)
	def calcular_distancia(self, otro_punto):
		"""Calcula la distancia desde este punto a un segundo pasado como un parámetro.
		Esta función usa el Teorema de Pitágoras para calcular la distancia entre puntos.
		La distancia es devuelta como un float."""
		# Usamos el teorema de Pitágoras para calcular la distancia entre dos coordenadas x,y
		# Para usamos la raiz cuadrada del cálculo entre paréntesis. No olvidemos que ** es 
		# elevar algo a un exponente. En este caso x**2 es elevar x al cuadrado
		return math.sqrt( 
			( self.x - otro_punto.x ) ** 2 +
			( self.y - otro_punto.y ) ** 2 )
		
help(Puntito)