from flask import redirect, url_for, render_template
from Macowin import app
from persistencia.persistencia import cargar_todos


@app.get("/listado_ventas")
def listado_vetas():
    return render_template("listado_ventas.html")