from flask import *
import feedparser

rss = feedparser.parse("https://rsshub.app/earthquake/ceic/2")
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", rss = rss)
