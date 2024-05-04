with open('input.txt') as f:
    data = f.read()
counter_dict = {}
for ch in data:
    if ch not in d:
        d[ch] = 1
    d[ch] += 1
with open('answer.txt', 'w') as file:
    for char, count in counter_dict.items():
        file.write(f"{char}: {count}\n")