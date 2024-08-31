import requests
from datetime import datetime
from pprint import pprint
coords = (55.01, 82.55)
API_KEY = 'd75a7ce31cbfc5ab1fc9efc22553d8a5'
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
with open('weather.json', 'w') as f:
    pprint(ans, f)

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
tmax = main['temp_max']
cld = ans['clouds']['all']

print(geo)
print(weather_desc)
print(f'Температура: {temp}, градусов Цельсия')
print(f'Ощущается как: {feels_like}, градусов Цельсия')
print(f'Максимальная температура: {tmax}, градусов Цельсия')
print(f'Облачность: {cld}%')
print(f'Влажность: {humidity}%')
print(f'Давление: {pressure}, Па')
print(f'Скорость ветра: {wind},  м/с')
print(f'Время восхода солнца: {sunrise}')
print(f'Время заката солнца: {sunset}')