# Кортежи - неизменяемая структура данных (как списки, только нельзя добавлять, удалять, обновлять элементы)

# Создаем кортеж

# objects_tuple = tuple()
# objects_tuple = ()
# objects_tuple = (1, 2, 3)
# print(type(objects_tuple))

# objects_tuple = tuple([1, 2, 3])
# print(objects_tuple, type(objects_tuple))

# ----------------------------------------------------------

# Кортежи и их возможности

# Работа с индексами в кортежах точно такая же, как и в списках
# objects_tuple = (1, 2, 3)
# first_elem = objects_tuple[0]
# print(first_elem)

# Кортежи нельзя изменять
# objects_tuple[0] = 5

# Распаковка кортежа
# objects_tuple = (1, 2, 3)
# first, second, third = objects_tuple
# print(first, second, third)

# Появится ошибка
# first, second = objects_tuple
# print(first, second)

# Появится ошибка
# first, second, third, fourth = objects_tuple
# print(first, second, third, fourth)

# Обход кортежа с помощью цикла for
# objects_tuple = (1, 2, 3)
# for elem in objects_tuple:
#     print(elem)

# ----------------------------------------------------------

# Методы кортежей

# У кортежей есть 2 метода - сount() и index() - работают также, как и со списками
# objects_tuple = (1, 2, 3)
# print(objects_tuple.count(2))
# print(objects_tuple.index(1))

# objects_tuple = (1, 2, 3, 1)
# print(objects_tuple.index(1))

# ----------------------------------------------------------

# Сложение кортежей (через оператор +)

# first_tuple = (1, 2)
# second_tuple = (3, 4)
# third_tuple = first_tuple + second_tuple
# print(third_tuple)

# Срезы работают также, как и со списками
# sliced_tuple = first_tuple[1:] + second_tuple[1:]
# print(sliced_tuple)

# ----------------------------------------------------------

# Кортежи и взаимодействие с функциями

# def func(a, b, c):
#     print(a, b, c)

# objects_tuple = (1, 2, 3)
# С помощью * происходит распаковка кортежа и передача аргументов в функцию
# func(*objects_tuple)

# Когда функция возвращает несколько значений через запятую - генерируется и возвращается кортеж
# def func(a, b, c):
#     summa = a + b + c
#     diff = a - b - c
#     return summa, diff

# objects_tuple = (1, 2, 3)
# result = func(*objects_tuple)
# print(type(result))

# summa, difference = func(*objects_tuple)
# print(summa, difference)

# ----------------------------------------------------------

# Кейсы применения кортежей

# empty_tuple = tuple()

# проверка, является ли кортеж пустым или нет
# if empty_tuple:
#     print('Кортеж не пустой')
# else:
#     print('Кортеж пустой')


# Чтобы создать кортеж из одного элемента, нужно рядом с элементом поставить запятую
# not_empty_tuple = (1,)

# if not_empty_tuple:
#     print('Кортеж не пустой')
# else:
#     print('Кортеж пустой')

# Если внутри кортежа хранятся изменяемые объекты, то их МОЖНО менять
# tuple_with_lists = ([1, 2, 3], [4, 5, 6])
# tuple_with_lists[0].append(4)
# print(tuple_with_lists)

# tuple_with_lists[0].remove(4)
# print(tuple_with_lists)

# first_list = tuple_with_lists[0]
# for i in range(10):
#     first_list.append(i)
# print(tuple_with_lists)

# tuple_with_lists[0].append(20)
# print(tuple_with_lists[0])
# print(first_list)

# ----------------------------------------------------------

# Кортеж vs Список

# import sys

# objects_list = []
# print(sys.getsizeof(objects_list))    # получаем 56

# objects_list = [1]    
# print(sys.getsizeof(objects_list))    # получаем 64

# objects_list = [1, 2]
# print(sys.getsizeof(objects_list))    # получаем 72

# objects_tuple = tuple()
# print(sys.getsizeof(objects_tuple))   # получаем 40

# objects_tuple = tuple(1,)
# print(sys.getsizeof(objects_tuple))   # получаем 48

# objects_tuple = tuple(1, 2)
# print(sys.getsizeof(objects_tuple))   # получаем 56 (разница со списком в 16 байт)

# objects_list = []
# for num in range(10000):
#     objects_list.append(num)
# print(sys.getsizeof(objects_list))    # получаем 85176

# objects_tuple = tuple(objects_list)
# print(sys.getsizeof(objects_tuple))   # получаем 80040 (разница со списком в 5176 байт)

# objects_list = []
# for num in range(10000000):
#     objects_list.append(num)
# print(sys.getsizeof(objects_list))    # получаем 89095160

# objects_tuple = tuple(objects_list)
# print(sys.getsizeof(objects_tuple))   # получаем 80000040 (разница со списком 9095120 байт)



