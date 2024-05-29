data = {  #создадим словарь с данными
    'Петя': {'Физика': 50, 'Математика': 80, 'Биология': 90}, 
    'Ваня': {'Математика': 65, 'Химия': 64, 'Физика': 90, 'РЯ': 78},
    'Катя': {'РЯ': 45, 'История': 57, 'Математика': 87},
}
for name, subjects in data.items(): #перебираем ключи и значения словаря
    print(f'{name}:{sum(subjects.values())}')

subjects_score = {}

for line in data.values():
    for subject in line.keys():
        if subject not in subjects_score: subjects_score[subject] = []
        subjects_score[subject].append(line[subject])

# from pprint import pprint
# pprint(subjects_score)
for subject, score in subjects_score.items():
    print(f"{subject}: {sum(score)/len(score)}")