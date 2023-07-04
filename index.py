from flask import *
import feedparser

rss = feedparser.parse("https://rsshub.app/earthquake/1")
lst = [{'title': entry['title'].encode('utf8').decode('unicode_escape'), 'description': entry['description'].encode('utf8').decode('unicode_escape')} for entry in rss['entries']]
app = Flask(__name__)
@app.route("/")
def index():
    return lst
