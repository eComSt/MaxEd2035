import requests
from datetime import datetime
API_KEY = 'd75a7ce31cbfc5ab1fc9efc22553d8a5'

def get_coords(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}'
    response = requests.get(url).json()
    return response[0]['lat'],response[0]['lon']


def get_weather(coords):
    url =url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {
        'lat': coords[0],
        'lon': coords[1],
        'appid': API_KEY,
        'units':'metric',
        'lang': 'ru'
    }

    response = requests.get(url, params=params)
    ans = response.json()
    lst = ['Страна', "Город", ]

    country = ans['sys']['country']
    town = ans['name']
    geo = f' Погода: {country}, {town}'
    weather_desc = ans['weather'][0]['description']
    main = ans['main']
    temp = main['temp']
    feels_like = main['feels_like']
    humidity = main['humidity']
    pressure = main['pressure']
    wind = ans['wind']['speed']
    sunrise = ans['sys']['sunrise']
    sunrise = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
    sunset = ans['sys']['sunset']
    sunset = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

    