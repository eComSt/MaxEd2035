import json

human = {
    'имя': 'Дима',
    'возраст': 18,
    'город': 'Moscow'
}
# with open('human.json', 'w', encoding='utf-8') as f:
#     json.dump(human, f, ensure_ascii=False, indent = 4)
# data = json.dumps(human, ensure_ascii=False, indent = 4)

# loaded_data = json.loads(data)

# print(loaded_data['имя'])

with open('example.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
if  (loaded_data["isFullTime"] == True and 
    len(loaded_data["progLanguages"])>1):
    print("Прходит на первый этап")
else:
    print("Не прходит на первый этап")