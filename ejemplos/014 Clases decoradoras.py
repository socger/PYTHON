#encoding: utf-8

# ******************************************************************************* #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# ******************************************************************************* #

'''
*********************************************************************************
** clases DECORADORaS.                                                        **
**                                                                            **
** Esta era antes la función decoradora                                       **
** def decorador(funcion):                                                    **
**      def funcionDecoradora(*args, **kwargs):                               **
**          print "Función ejecutada ", funcion.__name                        **
**          funcion(*args, **kwargs)                                          **
*********************************************************************************
'''

class Decorador(object):
    ''' Mi clase decoradora '''
    def __init__(self, funcion):
        self.funcion = funcion
        
    # Ahora tendremos un método llamado __call__ que es el que hace lo mismo que 
    # en una función decoradora
    # No hace falta llamar a __call__
    def __call__(self, *args, **kwargs):
        print "Función ejecutada ", self.funcion.__name__
        self.funcion(*args, **kwargs)

@Decorador
def resta(n,m):
    print n-m

resta(3,5)
