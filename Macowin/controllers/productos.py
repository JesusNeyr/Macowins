from flask import redirect, url_for, render_template,request
 
from Macowin import app
 
@app.route("/productos")
def products():
   return render_template("productos.html",buscar=request.args.get("buscar",""),precio=request.args.get("precio",""),categoria=request.args.get("categoria","todas"))

# @app.route("/productos",methods=['POST'])
# def products():
#    # precio_de_producto=request.form['precio']
#    return render_template("productos.html",precio=request.args.get("precio",""))