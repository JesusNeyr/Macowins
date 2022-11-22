from flask import Flask,request,render_template

app=Flask(__name__)

@app.get("/")
def hola_mundo():
    return print("Hola")