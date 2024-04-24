# Строки

# string = 'строка'
# another_string = "еще строка 123"

# -----------------------------------------------------

# f - строки
# for i in range(10):
#     print(f'i = {i}')

# -----------------------------------------------------

# Метод split() 
# syms = input()
# syms_list = syms.split()
# syms_list = syms.split(',')
# print(f'Количество символов в строке без пробелов = {len(syms_list)}')

# -----------------------------------------------------

# Метод replace()

# syms = input()
# cleaned_syms = syms.replace(' ', '')
# print(f'Количество символов в строке без пробелов = {len(cleaned_syms)}')

# syms = input()
# cleaned_syms = syms.replace(' ', ',')
# print(f'Количество символов в строке без пробелов, но с запятыми = {len(cleaned_syms)}')

# syms = input()
# cleaned_syms = syms.replace(',', ' ')
# print(f'Количество символов в строке без запятых, но с пробелами = {len(cleaned_syms)}')

# -----------------------------------------------------

# Метод join()

# hello_world = ['Привет', 'мир', '!']
# list_to_str = ''.join(hello_world)
# print(list_to_str)

# hello_world = ['Привет', 'мир', '!']
# list_to_str = ' '.join(hello_world)
# print(list_to_str)

# -----------------------------------------------------

# Метод count()
# string = 'abacaba'
# print(string.count('a'))
# print(string.count('aba'))

# -----------------------------------------------------------------------

# Работа с регистром символов строки
# Методы lower(), upper(), title(), capitalize()

# print('привет' == 'Привет!')

# city = input()
# if city == 'москва':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве :(')

# city = input()
# if city.lower() == 'москва':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве :(')

# city = input()
# if city.upper() == 'МОСКВА':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве :(')

# city = input()
# if city.capitalize() == 'Москва':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве :(')

# city = input()
# if city.title() == 'Нижний Новгород':
#     print('Мы готовы доставить заказ!')
# else:
#     print('К сожалению, заказ доставить не получится.')

#------------------------------------------------------------------

# Срезы строк
# string = 'abcdefg'
# print(string[0])
# print(string[-1])
# print(string[1:6])
# print(string[1:])
# print(string[1:6:2])
# print(string[6:1:-1])

#------------------------------------------------------------------

# Проверка наличия подстроки в основной строке

# city = 'Нижний Новгород'
# if 'Новгород' in city:
#     print('Такая подстрока есть')
# else:
#     print('Такой подстроки нет')

# ----------------------------------------------------------------

# Итерирование по строкам и метод isdigit()
# for sym in 'year2023':
#     if sym.isdigit():
#         print(sym)
