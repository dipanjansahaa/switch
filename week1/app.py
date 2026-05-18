from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "week 1 working till now"}

from services.weather import get_weather

@app.get("/weather/{city}")
def weather(city: str):
    return get_weather(city)

from services.news import get_news

@app.get("/news")
def news():
    return get_news()