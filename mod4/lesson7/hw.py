import requests
from datetime import timedelta
API_KEY = 'd75a7ce31cbfc5ab1fc9efc22553d8a5'

def get_coords(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}'
    response = requests.get(url).json()
    return response[0]['lat'],response[0]['lon']


def get_day(city):
    coords = get_coords(city)
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

    sunrise = ans['sys']['sunrise']
    sunset = ans['sys']['sunset']
    td = sunset - sunrise
    return timedelta(seconds=td)


print(get_day('Москва'))