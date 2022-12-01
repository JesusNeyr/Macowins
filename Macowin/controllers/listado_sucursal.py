from flask import redirect, url_for, render_template
from Macowin import app
from persistencia.persistencia import cargar_todos




@app.get("/listado_de_sucursales")
def lista_sucursales():
    
    return render_template("listado_de_sucursales.html", sucursales= cargar_todos().values())