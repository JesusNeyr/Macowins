from ast import Raise
from datetime import date
from operator import itemgetter
from textwrap import shorten
from producto.producto import *
from persistencia.persistencia import *
from sucursales.sucursal_fisica import*
from sucursales.sucursal_virtual import *
remera=Producto("remera adidas","remera",1,2000)
def alamacenar_datos_de_una_sucursal(nombre,una_sucursal):

    guardar(nombre,una_sucursal)

sucursales_guardadas=cargar_todos()

lista_de_sucursales=[]

for una_sucursal in sucursales_guardadas.values():
   lista_de_sucursales.append(una_sucursal)