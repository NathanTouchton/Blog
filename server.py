from random import randint
from datetime import date
from json import loads
from requests import get
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    year = date.today().year
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    parameters = {
        "name": name
    }
    age_response = get(url="https://api.agify.io", params=parameters, timeout=10)
    age_response.raise_for_status()
    age = loads(age_response.text)["age"]

    gender_response = get(url="https://api.genderize.io", params=parameters, timeout=10)
    gender_response.raise_for_status()
    gender = loads(gender_response.text)["gender"]
    print(gender)

    return render_template("name-game.html", name=name, age=age, gender=gender)
