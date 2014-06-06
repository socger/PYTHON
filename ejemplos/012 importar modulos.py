#encoding: utf-8

# ******************************************************************************* #
# IMPORTANTE ... NO OLVIDAR
# con la linea de arriba conseguimos utilizar los caracteres como
# la ñ por la consola y nos permitirán los acentos áà
# ******************************************************************************* #


'''
*********************************************************************************
** COMO IMPORTAR MODULOS.                                                      **
** Debemos de remarcar que pueden ser módulos nuestros creados anteriormente,  **
** módulos de terceros ó módulos propios de python                             **
**                                                                             **
** Se usa el comando "import nombre_del_modulo"	                               **
** Y a partir de este momento se pueden hacer llamadas a funciones del módulo  **
** importado ó instanciar clases de él, etc.                                   **
** El asunto es que cada vez que hagamos uso de algo de este módulo, tenemos   **
** que usar el nombre de la clase ó función, precedida del nombre del módulo   **
** importado                                                                   **
*********************************************************************************
** import database                                                             **
** db = database.Database()                                                    **
*********************************************************************************
** Con estas líneas de arriba hemos importado un módulo completo, pero puede   **
** que sólo queramos importar una clase de este módulo, en vez de cargar el    **
** módulo entero:                                                              **
*********************************************************************************
** from database import Database                                               **
** db = database.Database()                                                    **
*********************************************************************************
** Si deseamos cambiar el nombre de la clase usamos la cláusula "as"           **
*********************************************************************************
** from database import Database as DB                                         **
** db = DB()                                                                   **
*********************************************************************************
** Podemos también de una sola importación traernos más de una clase           **
*********************************************************************************
** from database import Database, Tabla                                        **
** db = Database()                                                             **
** tb = Tabla()                                                                **
*********************************************************************************
** Aunque no se recomienda su uso, también podríamos cargar todas las clases y **
** funciones de un módulo de esta manera:                                      **
*********************************************************************************
** from database import *                                                      **
** db = Database()                                                             **
** tb = Tabla()                                                                **
*********************************************************************************
**                                                                             **
** AHORA PASAREMOS A ORGANIZAR NUESTROS MODULOS( USO DE PAQUETES )             **
**                                                                             **
*********************************************************************************
** No se pueden poner módulos dentro de otros módulos, pero los módulos (que en**
** realidad son archivos con la extensión .py) pueden ir organizados por direc-**
** torios. Por lo que el nombre del paquete será el nombre del directorio      **
** Así que lo que hay que decirle a python es que un directorio es un paquete y**
** crear un archivo con el nombre "__init__.py" dentro del directorio paquete, **
** que normalmente irá vacío (este fichero es imprescindible). Si no existiera **
** este fichero no podríamos importar módulos desde este paquete.              **
*********************************************************************************
** El ejemplo está en el directorio "Escuela" y la estructura del directorio es**
**                                                                             **
** \escuela\         (directorio padre)                                        **
** \escuela\main.py                                                            **
**                                                                             **
** \escuela\escolar\            (directorio segundo nivel)                     **
** |escuela\escolar\__init_.py  (convierte el directorio en un paquete)        **
** |escuela\escolar\alumnos.py                                                 **
** |Escuela\escolar\database.py                                                **
**                                                                             **
** \escuela\escolar\calificaciones\          (directorio tercer nivel)         **
** \escuela\escolar\calificaciones\_init_.py (directorio en paquete)           **
** \escuela\escolar\calificaciones\examenes.py                                 **
** \escuela\escolar\calificaciones\trabajos.py                                 **
*********************************************************************************
** Por lo que ahora impera saber que en python hay dos tipos de imports, los   **
** absolute y los relative                                                     **
**                                                                             **
** En los import absolute tenemos que especificar la ruta completa al módulo ó **
** la clase que queremos importar. De tal manera que para importar la clase    **
** Alumno() que está dentro del módulo alumnos.py, que a su vez está dentro del**
** paquete/directorio escolar, podríamos usar varias síntaxis                  **
**                                                                             **
**    1) ... import escolar.alumnos.alumno = escolar.alumnos.Alumno()          **
**                                                                             **
**    2) ... from escolar.alumnos import Alumno                                **
**           alumno = Alumno()                                                 **
**                                                                             **
**    3) ... from escolar import alumnos                                       **
**           alumno = alumnos.Alumno()                                         **
**                                                                             **
** Como hemos visto los imports usan los puntos como separador                 **
*********************************************************************************
'''



