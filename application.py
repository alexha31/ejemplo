from flask import Flask, render template

app=Flak(__name__)

@app.route("/")
def index():
    return render_templates "index.html"