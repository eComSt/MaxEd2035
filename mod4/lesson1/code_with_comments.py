# Парсинг JSON-документа I

import json

# Функция dumps()

human = {
    'name': 'Dima',
    'age': 18,
    'city': 'Moscow'
}

human_json = json.dumps(human)
print(human_json)

# >>> {"name": "Dima", "age": 18, "city": "Moscow"}

human = {
    'имя': 'Дима',
    'возраст': 18,
    'город': 'Москва'
}

human_json = json.dumps(human, ensure_ascii=False)
print(human_json)

# >>> {"имя": "Дима", "возраст": 18, "город": "Москва"}

# -----------------------------------------------------------------------

# Функция dump()

human = {
    'name': 'Dima',
    'age': 18,
    'city': 'Moscow'
}

file = open('human.json', 'w')
json.dump(human, file)


human = {
    'имя': 'Дима',
    'возраст': 18,
    'город': 'Москва'
}

file = open('human.json', 'w', encoding='utf-8')
print(json.dumps(human, file, ensure_ascii=False, indent=4))

# -----------------------------------------------------------------------

# Функция loads()

human = {
    'имя': 'Дима',
    'возраст': 18,
    'город': 'Москва'
}
human_json = json.dumps(human, ensure_ascii=False)
print(json.loads(human_json))

# >>> {'имя': 'Дима', 'возраст': 18, 'город': 'Москва'}

# -----------------------------------------------------------------------

# Функция load()

file = open('human.json' , encoding='utf-8')
human_data = json.load(file)
print(human_data)

# >>> {'имя': 'Дима', 'возраст': 18, 'город': 'Москва'}

# human_json = json.dumps(human, ensure_ascii=False)
# print(human_json)

# -----------------------------------------------------------------------

# Проверка анкеты сотрудника

file = open('example.json', encoding='utf-8')
example_data = json.load(file)
if example_data['isFullTime'] == True and len(example_data['progLanguages']) >= 2:
    print('Проходит на 1 этап')
else:
    print('Не проходит на 1 этап')
