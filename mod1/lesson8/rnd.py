from random import randint

N = randint(10, 100)
with open('data.txt', 'w+',encoding="UTF-8") as file:
    for i in range(N):
        file.write(f'{randint(1,100)}\n')
    file.seek(0)
    numbers = []
    for line in file:
        numbers.append(int(line))
print(max(numbers), min(numbers))