from config import API_ID
import requests
import json
from aiogram.types import Message

def req(city):
    url="http://api.openweathermap.org/data/2.5/weather"

    params={
        "q":city,
        "appid": API_ID,
        "units": "metric",
        "lang": "ru"
    }

    try:
        response=requests.get(url,params=params)
        data=json.loads(response.text)

        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
    except Exception:
        print("Ошибка при получении")

    result=f"В городе {city} {weather_desc} {temperature} С*\n Остановить /cancel"
    return result




