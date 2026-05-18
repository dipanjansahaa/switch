import requests

API_KEY = "de235b990e53b9ae214c948994784cb3"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    return response.json()