#encoding: utf-8

# *********************************************************************************** #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# *********************************************************************************** #


''' ***********************************************************************************
ENCAPSULACION
Es la idea de que ciertos variables, funciones, métodos o atributos sean públicos 
o privados
Por ejemplo en una clase si instanciamos una variable, un atributo o un método como
privado, los objetos no podrán acceder a ellos desde fuera de la clase.
***********************************************************************************
Un método se considera como privado si se inicia su nombre con dos guiones bajos. 
Pero hay que tener muy en cuenta de que si un método se inicia con dos guiones
bajos, no puede ser finalizado (su nombre) con dos guiones bajos. Estos métodos son 
métodos especiales como el def __init__(self) ... el constructor
*************************************************************************************** '''
class Prueba(object):
	def __init__(self):
		self.__atributo_privado = 'Soy privado y soy un atributo' # Atributo privado
		self.atributo_publico = 'Soy público y soy un atributo'   # Atributo público

	def __metodoPrivado(self): # Método privado
		print 'soy privado y soy un método'

	def metodoPublico(self):   # Método público
		print 'Soy publico y soy un método'

	# Esta es una manera de acceder a un método privado
    # Evidentemente sólo se puede acceder desde la clase
    # y lo hacemos usando el self
	def AccederMetodoPrivado(self):
		self.__metodoPrivado()

	def getAtributoPrivado(self):
		return self.__atributo_privado # Así podríamos devolver el valor de un atributo/variable privada

	# Esta es una manera de actualizar los vlores de un atributo privado
	def set_Atributo_Privado(self, valor):
		self.__atributo_privado = valor

objeto = Prueba()

print objeto.atributo_publico
# print objeto.__atributo_privado ... esta sentencia daría un error porque es un atributo (variable) privado

# objeto.__metodoPrivado() ... esta setencia daría un error porque es un método privado
objeto.metodoPublico()

objeto.AccederMetodoPrivado()

print objeto.getAtributoPrivado()

# Como actualizar un atributo de la clase Prueba si es privado
objeto.set_Atributo_Privado('Tengo un nuevo valor')
print objeto.getAtributoPrivado()

''' En python no existe la sobre carga de métodos, aunque permite tener en una clase
varios métodos iguales. Lo que pasa es que en realidad se queda con el último método
llamado igüal. Es decir que si creo tres métodos llamados pepe, y con lineas diferentes
de código, si llamo desde un objeto al método pepe, sólo ejecutará las líneas del 
último método creado con nombre pepe '''

''' En python tampoco existe el polimorfismo '''
