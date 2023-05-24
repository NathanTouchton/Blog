from random import randint
from datetime import date
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
    age = age_response.json()["age"]

    gender_response = get(url="https://api.genderize.io", params=parameters, timeout=10)
    gender_response.raise_for_status()
    gender = gender_response.json()["gender"]

    return render_template("name-game.html", name=name, age=age, gender=gender)

@app.route("/blog")
def blog():
    blog_response = get(url="https://api.npoint.io/c790b4d5cab58020d391", timeout=10)
    blog_response.raise_for_status()
    text = blog_response.json()
    return render_template("blog.html", text=text)