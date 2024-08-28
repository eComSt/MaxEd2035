def separator(symbol='', length=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(symbol * length)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@separator('-', 20)
def say_hello(name):
    return f'Добрый день, {name}'

@separator('+', 30)
def say_bye(name):
    return f'До свидания, {name}'

print(say_hello('Дима'))
print(say_bye('Дима'))