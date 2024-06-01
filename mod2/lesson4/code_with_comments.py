# Генераторы списков и словарей

# numbers = []
# for num in range(1, 100001):
#     numbers.append(num)

# создаем генератор списков
# numbers = [num for num in range(1, 100001)]
# print(numbers)

# ---------------------------------------------------------

# Задача с генерацией квадратов натуральных чисел от 1 до N

# N = int(input())
# squares = [num**2 for num in range(1, N + 1)]
# print(squares)

# squares = [num**2 for num in range(1, int(input()) + 1)]
# print(squares)

# ---------------------------------------------------------

# Задача про отдельные символы строки
# line = input()
# symbols = [sym for sym in line]
# print(symbols)

# symbols = [sym for sym in input()]
# print(symbols)

# ---------------------------------------------------------

# Генерация списка с условием if

# Задача про отбор элементов кратных 7
# numbers = [num for num in range(100, 1001) if num % 7 == 0]

# ---------------------------------------------------------

# Задача про города на букву А и длиной не менее 7 символов
# cities = ['Самара', 'Москва', 'Анапа', 'Новосибирск', 'Архангельск', 'Екатеринбург', 'Александровск']
# new_cities = [city for city in cities if city[0] == 'А' and len(city) >= 7]
# print(new_cities)

# ---------------------------------------------------------

# Задача про города с неповторяющимися буквами
# cities = ['Самара', 'Москва', 'Анапа', 'Новосибирск', 'Архангельск', 'Екатеринбург', 'Александровск']
# uniq_cities = [city for city in cities if len(city) == len(set(city.lower()))]
# print(uniq_cities)

# ---------------------------------------------------------

# Генерация словарей

# Словарь с корнями натуральных чисел
# from math import sqrt

# square_roots = {}
# for num in range(1, 21):
#     # square_roots[num] = sqrt(num)
#     square_roots[num] = num**0.5

# square_roots = {num:num**0.5 for num in range(1, 21) if num % 2 == 0}

# print(square_roots)

# ---------------------------------------------------------

# Задача про переоценку фруктов

# fruits = {
#     'Персики': 150,
#     'Яблоки': 100,
#     'Бананы': 140,
#     'Лимоны': 200,
#     'Авокадо': 450
# }

# fruits_new = {fruit:price * 1.2 for fruit, price in fruits.items()}
# print(fruits_new)

# ---------------------------------------------------------

# Генерация вложенных списков и словарей

# Задача про фрагмент таблицы умножения

# N = int(input())
# table = []
# for i in range(1, N + 1):
#     line = []
#     for j in range(1, N + 1):
#         line.append(i * j)
#     table.append(line)

# for line in table:
#     print(line)

# N = int(input())
# table = [[i * j for j in range(1, N + 1)] for i in range(1, N + 1)]

# ---------------------------------------------------------

# Задача про числа и их делители

# from time import time

# def get_divisors(n):
#     divisors = []
#     for div in range(2, n // 2 + 1):
#         if n % div == 0:
#             divisors.append(div)
#     return divisors

# N, M = int(input()), int(input())
# start = time()

# nums_and_divs = {num:get_divisors(num) for num in range(N, M + 1) if len(get_divisors(num)) > 0}

# stop = time()
# print(f'Программа работала {stop - start} секунд')

# ---------------------------------------------------------

# N, M = int(input()), int(input())
# start = time()

# nums_and_divs = {}
# for num in range(N, M + 1):
#     divs = get_divisors(num)
#     if len(divs) > 0:
#         nums_and_divs[num] = divs

# stop = time()
# print(f'Программа работала {stop - start} секунд')