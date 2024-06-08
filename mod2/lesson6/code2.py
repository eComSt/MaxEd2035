check = True
while check:
    try:
        a = int(input())
        b = int(input())
        ans = a % b
    except ZeroDivisionError:
        print('Делить на ноль нельзя, введите новые числа:')
    except ValueError:
        print("Некорректные данные!")
    else:
        check = False

ans = a % b # повторно вычисляем остаток от деления
print(f'Остаток от деления: {ans}')