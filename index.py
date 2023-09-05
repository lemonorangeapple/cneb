from flask import *
import feedparser

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", rss = feedparser.parse("https://rsshub.app/cneb/yjxx"))

@app.route("/<path:path>")
def subpath(path):
    return render_template("index.html", rss = feedparser.parse(f"https://rsshub.app/cneb/yjxx/{path}"))
