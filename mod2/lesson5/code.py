words = ['четыре', 'восемь', 'пятнадцать', 'восемнадцать']
max_word = ''#создаем пустую строку для хранения самого длинного слова
for word in words: #перебираем строки в списке
    if len(word) > len(max_word): #если длина текущей строки больше 
        max_word = word #обновляем значение переменной
# print(max_word) #выводим итоговое значение на экран
# print(max(words,key=len))
# def mod(x):
#     if x<0: x = -x
#     return x
# w = [1,2,3,4,-5,-8,7]
# print(max(w,key = mod))
# # x = int(input())
# # def double(x):
# #     return x * 2
# double = lambda x,y: x*y
# print(double(2,5))

d = ['4', '23', '15', '8']
max_str = 0
for num in d:
    if int(num)> int(max_str):
        max_str = num
# print(max([int(i) for i in d]))
# print(max_str)

# print(max(d,key = int))

d = ['4', '23', '15', '8']
# d2 = [int(i) for i in d]
d2 = list(map(int,d))
# print(d2)

# base = [1, 2, 5, 6] #список с основаниями
# exp = [2, 3, 4, 5] #список с показателями
# data = list(map(lambda x, y: x**y, base, exp))
# print(data)


# words = ['красный', 'синий', 'оранжевый', 'белый']
# #указываем последовательность, из которой будем брать данные
# long_words = list(filter(lambda line: len(line) > 5, words))
# print(long_words)

# words = ['шалаш', 'кот', 'топот', 'бег']
# pal_words = list(filter(lambda word: word == word[::-1], words))
# print(pal_words)

from functools import reduce #подключаем функцию reduce() 
numbers = [1, 2, 3, 4, 5,1,3,4,6,7,4,3,5,7] #задаем список с числами
#в переменной mult сохраняем произведение элементов списка numbers
mult = reduce(lambda x, y: x * y, numbers)
print(mult)