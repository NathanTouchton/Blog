from flask import Flask, render_template

app = Flask(__name__)

###Using the API for our blog posts we created on n:Point,
# render all the blogs' title and subtitles on the home page.###

###Make a "Read" anchor tag at the end of each blog post preview link to a page with the entire blog - title, subtitle and body.
# The individual blog posts should live at the path: URL/post/blog_id###

@app.route('/')
def home():
    return render_template("index.html")
