number_1 = input('Введите 1-е число:')
number_2 = input('Введите 2-е число:')

if number_1.isnumeric() and number_2.isnumeric():
    number_1 = int(number_1)
    number_2 = int(number_2)

    oper = input('Введите операцию:')

    if oper == "+":
        result = number_1 + number_2
        print('Сумма:', result)
    elif oper == "-":
        result = number_1 - number_2
        print('Разность:', result)
    elif oper == "*":
        result = number_1 * number_2
        print('Произведение:', result)
    elif oper == "/":
        if number_2 == 0:
            print("На ноль делить нельзя")
        else:
            result = number_1 / number_2
            print('Частное:', result)
    elif oper == "//":
        if number_2 == 0:
            print("На ноль делить нельзя")
        else:
            result = number_1 // number_2
            print('Частное(целая часть):', result)
    elif oper == "%":
        if number_2 == 0:
            print("На ноль делить нельзя")
        else:
            result = number_1 % number_2
            print('Частное(остаток):', result)
