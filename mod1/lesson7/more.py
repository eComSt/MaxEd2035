# Функции

# Пример № 1
# Вывести на экран следующие значения:
# - сумма всех элементов
# - среднее арифм. всех элементов
# - макс. значение
# - мин. значение

# def show_info(lst):
#     print(f'Сумма: {sum(lst)}')
#     print(f'Среднее арифметическое: {sum(lst) / len(lst)}')
#     print(f'Максимальное значение: {max(lst)}')
#     print(f'Минимальное значение: {min(lst)}')

# основное тело программы
# numbers = []

# for i in range(10):
#     num = int(input())
#     numbers.append(num)

# show_info(numbers)

# numbers_1 = [12, 5, 456, -15, 64, 54, -124]

# show_info(numbers_1)

# -----------------------------------------------------------------

# Пример № 2
# С клавиатуры подается натуральное число, 
# функция находит и выводит на экран сумму всех цифр заданного числа
# 123 -> 6

# def sum_digits(num):
#     summa = 0
#     while num > 0:
#         summa += num % 10
#         num = num // 10
#     return summa
    
# print(f'Вывод на экран вне функции: {sum_digits(45345)}')

# -----------------------------------------------------------------

# Работа с аргументами функции

# функция без аргументов
# def send_hello():
#     print('Добрый день, пользователь!')
#     print('Хорошего вам дня!')


# def circle_area(rad=1):
#     pi = 3.14
#     return pi * rad**2

# result = circle_area(2)
# print(result)
# -----------------------------------------------------------------

# Рекурсивные функции

# F(n) = 10 - F(n - 1)
# def F(n):
#     return 10 - F(n - 1)

# print(F(5))

# F(n) = 10 - F(n - 1)
# F(1) = 1
# def F(n):
#     if n == 1:
#         return 1
#     else:
#         return 10 - F(n - 1)

# print(F(5))

# -----------------------------------------------------------------

# Работа с библиотеками в Python

# import math
# result = math.sqrt(25)
# print(result)
# print(dir(math))

# from math import *

# result = sqrt(25)
# print(result)

# from random import randint

# rand_num = randint(1, 100)
# print(rand_num)
