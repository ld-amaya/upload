from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "iamlou"


@app.route('/')
def home():
    return render_template("index.html")
