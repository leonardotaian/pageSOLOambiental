from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")


app.run(debug=True)

