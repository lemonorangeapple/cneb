from flask import *
import feedparser

rss = feedparser.parse("https://rsshub.app/earthquake/1")
app = Flask(__name__)
@app.route("/")
def index():
    return rander_template("index.html", rss = rss)