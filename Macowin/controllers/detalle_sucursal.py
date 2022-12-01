from flask import redirect, url_for, render_template
from Macowin import app
from persistencia.persistencia import cargar_todos

def todos_los_productos():
    productos = []
    for sucursal in cargar_todos().values():
        productos += sucursal.productos
    return productos

@app.get("/detalle_sucursal")
def detalle_sucursal():
    return render_template("detalle_sucursal.html")