from flask import redirect, url_for, render_template
 
from hmf import app
 
@app.get("/productos")
def products():
   return render_template("productos.html")