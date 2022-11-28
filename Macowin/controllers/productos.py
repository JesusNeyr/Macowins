from flask import redirect, url_for, render_template, request
from persistencia.persistencia import cargar_todos

from Macowin import app
# # lista de diccionarios
# productos={"nombre":"remera",
#             "precio":2000,
#             "id":2,
#             "categoria":"Short xs",
# }

def todos_los_productos():
    productos = []
    for sucursal in cargar_todos().values():
        productos += sucursal.productos
    return productos

def validar_precio():
   precio=request.args.get("precio", 0)
   if precio=="":
      return 0
   return int(precio)
@app.route("/productos")
def products():
    productos = todos_los_productos()
    print(productos)
    return render_template("productos.html",
                           buscar=request.args.get("buscar", ""),
                           precio=validar_precio(),
                           categoria=request.args.get("categoria", "todas"),
                           productos_all=productos)

# @app.route("/productos",methods=['POST'])
# def products():
#    # precio_de_producto=request.form['precio']
#    return render_template("productos.html",precio=request.args.get("precio",""))
