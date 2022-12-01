from flask import Flask

app = Flask(__name__)

import Macowin.controllers.home
import  Macowin.controllers.productos
import Macowin.controllers.detalle_sucursal
import Macowin.controllers.listado_sucursal
from Macowin import *