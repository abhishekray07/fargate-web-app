import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "cbdb357849b049ef9bd771a456536e5e"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=%s" % API_KEY

def get_news_articles():
    """Returns the list of news articles."""
    # fetch news articles from the api
    response = requests.get(NEWS_API_URL)

    # return the articles in JSON format
    return response.json()['articles']


@app.route('/')
def index():
    return str(get_news_articles())
