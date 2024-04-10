print('Привет мир')

number = 1000000
my_string = 'Очень важная строка'
print(my_string)

name = input('Представьтесь, пожалуйста:')
print('Привет, ' + name)

first_name = input('Как вас зовут?')
last_name = input('Какая у вас фамилия?')
patronymic = input('Какое у вас отчество?') 
print('Здравствуйте, ' + last_name + ' ' + first_name + ' ' + patronymic)
print('Здравствуйте, ', last_name, first_name, patronymic)

number_1 = 2432648923
number_2 = 6276
# сложение
print(number_1 + number_2)
# вычитание
print(number_1 + number_2)

number_1 = input()
number_2 = input()
print(type(number_1))
print(type(number_2))

# Калькулятор

number_1 = int(input('Введите первое число:'))
number_2 = int(input('Введите второе число:'))

summ = number_1 + number_2
diff = number_1 - number_2
mult = number_1 * number_2
div1 = number_1 / number_2
div2 = number_1 // number_2
div3 = number_1 % number_2
exp = number_1 ** number_2

print(type(summ))
print(type(diff))

print('Сумма:', summ)
print('Разность:', diff)
print('Произведение:', mult)
print('Частное от деления:', div1)
print('Целая часть от деления:', div2)
print('Остаток от деления:', div3)
print('Возведение в степень:', exp)


