from flask import redirect, url_for, render_template
 
from hmf import app
 
@app.get("/")
def raiz():
   return render_template("home.html")