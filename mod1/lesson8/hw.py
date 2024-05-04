with open('input.txt') as f:
    data = f.read()
counter_dict = {}
for ch in data:
    if ch not in counter_dict:
        counter_dict[ch] = 1
    counter_dict[ch] += 1
with open('answer.txt', 'w') as file:
    for char, count in counter_dict.items():
        file.write(f"{char}: {count}\n")