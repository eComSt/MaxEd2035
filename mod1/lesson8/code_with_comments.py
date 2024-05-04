# Работа с текстовыми файлами

# Открытие текстового файла

# file = open('file.txt')
# print(file)

# Cчитывание данных из файла

# file = open('file.txt')
# data = file.read()
# print(data)

# data = file.read()
# print(data)

# data = file.readline()
# print(data)

# data = file.readlines()
# print(data)

# ---------------------------------------------------------

# Закрытие файла

# file.close()

# ---------------------------------------------------------

# Работа с текстовой информацией

# file = open('file.txt')
# data = file.readline()
# print(data)

# file = open('file.txt', encoding='utf-8')
# data = file.readline()
# print(data)

# ---------------------------------------------------------

# Итерирование по текстовому файлу

# file = open('file.txt', encoding='utf-8')
# for line in file:
#     print(line)

# file = open('file.txt')
# summa = 0
# for num in file:
#     summa += num
# print(summa)

# file = open('file.txt')
# numbers = []
# for num in file:
#     numbers.append(int(num))
# print(sum(numbers))

# ---------------------------------------------------------

# Режимы работы с файлами

# file = open('file.txt', mode='w')
# file = open('file.txt', 'w')
# file.write('Hello, world!')

# file = open('file.txt', mode='a', encoding='utf-8')
# file.write('Привет, мир!')
# file.write('\nДобрый день!')

# ---------------------------------------------------------

# Решение практических задач

# Задача № 1

# file = open('nums.txt', mode='w')
# for num in range(1, 21):
#     file.write(f'{num}\n')
# file.close()

# ---------------------------------------------------------

# Задача № 2

# from random import randint

# file = open('rand_nums.txt', mode='w')
# N = randint(10, 100)
# for num in range(N):
#     file.write(f'{randint(1, 100)}\n')

# file = open('rand_nums.txt')
# numbers = []
# for num in file:
#     numbers.append(int(num))
# print(max(numbers) + min(numbers))

# ---------------------------------------------------------

# from random import randint

# file = open('rand_nums.txt', mode='w+')
# N = randint(10, 100)
# for num in range(N):
#     file.write(f'{randint(1, 100)}\n')

# file.seek(0)
# numbers = []
# for num in file:
#     numbers.append(int(num))
# print(max(numbers) + min(numbers))
