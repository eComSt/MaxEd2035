from functools import wraps
def my_function():
    '''Это строка документации. Здесь можно описать назначение функции'''
    return 'Привет!'

# print(my_function.__name__)
# print(my_function.__doc__)

def value(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)} рублей.'

    return wrapper



@value
def quad(price):
    '''Функция увкличивает значение в 4 раза'''
    return price*4
print(quad.__name__)
print(quad.__doc__)
print(quad(500))