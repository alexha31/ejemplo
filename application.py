from flask import Flask

app=Flak(__name__)

@app.route("/")
def index():
    return "¡Hola, mundo!"