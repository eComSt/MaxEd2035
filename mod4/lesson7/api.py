import requests
from datetime import datetime
API_KEY = 'd75a7ce31cbfc5ab1fc9efc22553d8a5'

def get_coords(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}'
    response = requests.get(url).json()
    return response[0]['lat'],response[0]['lon']


def get_weather(city):
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
    
    lst = ['Страна', "Город", "Температура, C", 
           "Ощущается как, C", "Максимальная температура, C",
           "Влажность, %", "Давление, Pa", "Ветер, м/с",
            "Облачность, %",  "Восход", "Закат", 
    ]

    country = ans['sys']['country']
    town = ans['name']
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

    resp = {'Страна':country, "Город":town, "Температура, C":temp, 
           "Ощущается как, C":feels_like, "Влажность, %":humidity, "Давление, Pa":pressure,
             "Ветер, м/с":wind, "Восход":sunrise, "Закат":sunset,
             "Максимальная температура, C":tmax, "Облачность, %":cld,
    }
    return '\n'.join([f'{key}: {resp[key]}' for key in lst])


print(get_weather('Новосибирск'))