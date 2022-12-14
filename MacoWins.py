from ast import Raise
from datetime import date
from operator import itemgetter
from textwrap import shorten
from producto.producto import *
from persistencia.persistencia import *
from sucursales.sucursal_fisica import*
from sucursales.sucursal_virtual import *


una_sucursal_fisica=SucursalFisica()

pantalon=Producto("pantalon","gala",1,123)

camisa=Producto("camisa","casual",2,1235)

short=Producto("short","sport",3,12345)

una_sucursal_fisica.registrar_producto(pantalon)

una_sucursal_fisica.registrar_producto(camisa)

una_sucursal_fisica.registrar_producto(short)

una_sucursal_fisica.recargar_stock(3,80)


una_sucursal_virtual=Sucursalvirtual()

una_sucursal_virtual.registrar_producto(pantalon)

una_sucursal_virtual.registrar_producto(short)


def alamacenar_datos_de_una_sucursal(nombre,una_sucursal):
    guardar(nombre,una_sucursal)


# Ahora en la terminal podés escribir estas líneas, en función de lo que quieras probar
# Tené en cuenta que este archivo te conviene cargarlo como python -i MacoWins.py
# Y que si borrás los pickles generados, se borrarán también de la persistencia
# alamacenar_datos_de_una_sucursal("fisica", una_sucursal_fisica)
# alamacenar_datos_de_una_sucursal("virtual", una_sucursal_virtual)