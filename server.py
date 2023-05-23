from random import randint
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    year = date.today().year
    return render_template("index.html", num=random_number, year=year)
