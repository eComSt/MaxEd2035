import json

# with open('countries_languages.json', 'r', encoding='utf-8') as f:
#     loaded_data = json.load(f)

# data = {}
# for i in loaded_data:
#     if i['language'] in data:
#         data[i['language']].append(i['country'])
#     else:
#         data[i['language']] = [i['country']]
# print(data) 

# f = open('countries_languages.json', 'r', encoding='utf-8')
# loaded_data = json.load(f)
# f.close()

class File(object):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with File('countries_languages.json', 'r') as f:
    loaded_data = json.load(f)

data = {}
for i in loaded_data:
    if i['language'] in data:
        data[i['language']].append(i['country'])
    else:
        data[i['language']] = [i['country']]
print(data)    


