import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def get_news():

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])

    headlines = []

    for article in articles:
        headlines.append({
            "title": article["title"],
            "source": article["source"]["name"]
        })

    return headlines