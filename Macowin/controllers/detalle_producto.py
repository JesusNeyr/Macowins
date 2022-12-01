from flask import redirect, url_for, render_template
from Macowin import app
from persistencia.persistencia import cargar_todos


@app.get("/detalle_producto")
def detalle_producto():
    return render_template("detalle_producto.html")