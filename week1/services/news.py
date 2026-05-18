import requests

API_KEY = "89ef54671bf249869df5f5e8970795ab"

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