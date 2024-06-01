# numbers = []
# for num in range(1, 100001):
#     numbers.append(num)

# numbers = [num**2 for num in range(1, 11) if num%2 == 0]
# print(numbers)
# N = int(input())+1
# # numbers = []
# # for num in range(1, N):
# #     numbers.append(num**2)
# # numbers = [num**2 for num in range(1, N)]
# numbers = [num**2 for num in range (1, N)]
# print(numbers)
# line = input()
# # ctrl+/
# symbols = [sym for sym in line]
# print(symbols)
cities = ['Самара', 'Москва', 'Анапа', 'Новосибирск', 'Архангельск', 'Екатеринбург', 'Александровск']
# new_cities = [city for city in cities if city[0] == 'А' and len(city) >= 7]
# print(new_cities)
# uniq_cities = [city for city in cities if len(city) == len(set(city.lower()))]

# print(uniq_cities)

# square_roots = {}
# for num in range(1, 21):
#     square_roots[num] = num**0.5

# print(square_roots)
# square_roots = {num:num**0.5 for num in range(1, 21) if num % 2 == 0}

# print(square_roots)

fruits = {
    'Персики': 150,
    'Яблоки': 100,
    'Бананы': 140,
    'Лимоны': 200,
    'Авокадо': 450
}
fruits_new = {fruit:price * 1.2 for fruit, price in fruits.items()}

# print(fruits_new)
# N = int(input())
# table = [[i * j for j in range(1, N + 1)] for i in range(1, N + 1)]
# for line in table:
#     print(*line)
from time import time          # импортируем функцию для работы со временем работы программы
def get_divisors(n):           # функция для поиска делителей
    divisors = []                     # список для хранения делителей
    for div in range(2, n // 2 + 1):  # перебираем делители от 2 до половины числа
        if n % div == 0:              # если нашли делитель
            divisors.append(div)      # добавляем делитель в список
    return divisors                   # возвращаем список с делителями
N, M = int(input()), int(input()) # вводим числа N и M
# start = time()                 # начальная временная метка
# словарь, где ключ – число, значение – список делителей числа
# nums_and_divs = {num:get_divisors(num) for num in range(N, M + 1) if len(get_divisors(num)) > 0}
# stop = time()                  # конечная временная метка
# print(f'Программа работала {stop - start} секунд') # выводим время генерации словаря
N, M = int(input()), int(input()) # вводим числа N и M
start = time()                 # начальная временная метка
nums_and_divs = {}             # словарь, где ключ – число, значение – список делителей числа
for num in range(N, M + 1):    # перебираем числа от N до M включительно
    divs = get_divisors(num)       # получаем список делителей числа
    if len(divs) > 0:          # если в списке есть хотя бы один делитель
        nums_and_divs[num] = divs # добавляем новый объект в словарь
stop = time()                  # конечная временная метка
print(f'Программа работала {stop - start} секунд') # выводим время генерации словаря