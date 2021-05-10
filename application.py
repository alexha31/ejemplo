from flask import Flask, redirect, url_for

app=Flak(__name__)

@app.route("/")
def index():
    return render_templates "index.html"