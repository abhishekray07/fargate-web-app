import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = ""
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=%s" % API_KEY

def get_news_articles():
    """Returns the list of news articles."""
    # fetch news articles from the api
    try:
        response = requests.get(NEWS_API_URL)
        # return the articles in JSON format
        return response.json()['articles']
    except Exception:
        return "Hello, world"


@app.route('/')
def index():
    return str(get_news_articles())
