import json
with open('countries_languages.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print(loaded_data)
data = {}
for i in loaded_data:
    print(i['country'])
    if i['language'] in data:
        data[i['language']].append(i['country'])
    else:
        data[i['language']] = [i['country']]

print(data)