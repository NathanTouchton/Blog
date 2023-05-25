from requests import get
from flask import Flask, render_template

app = Flask(__name__)

###Using the API for our blog posts we created on n:Point,
# render all the blogs' title and subtitles on the home page.###

response = get(url="https://api.npoint.io/c790b4d5cab58020d391", timeout=10)
response.raise_for_status()

blog_posts = response.json()

###Make a "Read" anchor tag at the end of each blog post preview link to a page with the entire blog
# - title, subtitle and body.
# The individual blog posts should live at the path: URL/post/blog_id.###

@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)

@app.route("/post/<number>")
# I think the issue lies with getting the post number.
def post_func(number):
    return render_template("post.html")
