# Пример № 2
# С клавиатуры подается натуральное число, 
# функция находит и выводит на экран сумму всех цифр заданного числа
# 123 -> 6

def sum_digits(n):
    summ = 0#123
    n = int(n)
    while n > 0:
        summ += n % 10 #3
        n //= 10 #12
    return summ

inp = input()
ans = sum_digits(inp)
print(ans)