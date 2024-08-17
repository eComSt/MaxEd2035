import requests
from pprint import pprint
coords = (55.0415, 82.9346)
API_KEY = 'KEY'
url = "https://api.weather.yandex.ru/v2/forecast?"

headers = {'X-Yandex-API-Key': API_KEY}

params = {'lat': coords[0],
          'lon': coords[1],
          'lang': 'ru_RU',

}

response = requests.get(url, headers=headers, params=params)
# print(response.json())
data = response.json()
fact = data['fact']

is_thunder = {
    False: 'Грозы нет',
    True: 'Гроза есть'
}

prec_type = {
    0: 'без осадков',
    1: 'дождь',
    2: 'дождь со снегом',
    3: 'снег',
    4: 'град'
}
prec_strength = {
    0: 'без осадков',
    0.25: 'слабый дождь/слабый снег',
    0.5: 'дождь/снег',
    0.75: 'сильный дождь/сильный снег',
    1: 'сильный ливень/очень сильный снег'
}


print(f'Температура {fact["temp"]} ℃')
print(is_thunder[fact['is_thunder']])
print(f"Тип осадков:{prec_type[fact['prec_type']]}")
print(f"Сила осадков:{prec_strength[fact['prec_strength']]}")