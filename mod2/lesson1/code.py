# Множества

# Структура данных set

# Пустое множество создается ТОЛЬКО через функцию set()
# my_set = set()
# my_set_2 = {1, 2, 3}

# print(type(my_set_2))

# -----------------------------------------------------------

# Добавление и удаление данных из множества

# my_set = set()
# add() - добавить элемент в множество
# my_set.add(1)
# my_set.add(2)
# my_set.add(3)
# print(my_set)

# discard() - удалить элемент из множества
# my_set.discard(1)
# my_set.discard(2)
# my_set.discard(3)
# print(my_set)

# Заполнение множества через цикл for
# for i in range(100):
#     my_set.add(i)
# print(my_set)

# clear() - очищение множества 
# my_set.clear()
# print(my_set)

# -----------------------------------------------------------

# Ограничения, связанные с множествами
# К элементам множества нельзя обращаться по индексу
# Внутри множества могут храниться только НЕИЗМЕНЯЕМЫЕ структуры данных(числа, строки)

# my_set = {1, 2, 3}
# print(my_set[0])

# my_set.add([4, 5])

# -----------------------------------------------------------

# Пересечение, объединение и вычитание множеств

# my_grades = {3, 4, 5}
# your_grades = {2, 4, 5}

# intersection() - пересечение множеств
# print(my_grades.intersection(your_grades))
# print(your_grades.intersection(my_grades))

# union() - объединение множеств
# print(my_grades.union(your_grades))

# difference() - вычитание множеств
# diff_grades = your_grades.difference(my_grades)
# Методы intersection(), union(), difference() не меняют исходные множества, а создают новое множество
# print(diff_grades)

# Методы intersection_update(), update(), difference_update() работают также, как их аналоги, но меняют исходное множество
# my_grades.intersection_update(your_grades)
# print(my_grades)
# my_grades.update(your_grades)
# my_grades.difference_update(your_grades)

# -----------------------------------------------------------

# Кейсы применения множеств

# В множествах хранятся только УНИКАЛЬНЫЕ (не повторяющиеся) элементы

# my_list = [1, 2, 3, 3, 1, 2, 4, 5]
# for i in set(my_list):
#     print(i)

# print(set(my_list))

# str1 = 'I love cats'
# str2 = 'c a t s'
# issubset() - метод, проверяющий являются ли одно множество подмножеством другого
# if set(str2).issubset(str1):
#     print('Да, является')
# else:
#     print('Нет, не является')

# issuperset() - метод, проверяющий, является ли одно множество супер-множеством для другого
# if set(str1).issuperset(str2):
#     print('Да')
# else:
#     print('Нет')

# -----------------------------------------------------------

# Угадай число

# n = int(input())
# result = set()
# for i in range(1, n + 1):
#     result.add(i)

# while True:
#     ask = input()
#     if ask == 'HELP':
#         print(result)
#         break
#     else:
#         ask_set = set()
#         for elem in ask.split():
#             ask_set.add(int(elem))
#     answer = input()
#     if answer == 'YES':
#         result.intersection_update(ask_set)
#     elif answer == 'NO':
#         result.difference_update(ask_set)



