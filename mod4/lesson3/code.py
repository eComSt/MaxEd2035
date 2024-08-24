from time import time, sleep
def decorator(func):
    def wrapper():
        print("func begin")
        func()
        print("func end")
    return wrapper

# @decorator
def main():
    print("Main is running")
    return 6
# main = decorator(main)

def tdecorator(func):
    def wrapper():
        t = time()
        func()
        print(time()-t)
    return wrapper

@tdecorator
def func():
    sleep(3)

# func()

def repeat(func):
    def wrapper(*args, **kwargs):
        for i in range(10):
            func(*args, **kwargs)
    return wrapper

@repeat
def message(name):
    print(f'hello {name}')

# message('Mihail')


def access(func):
    def wrapper(*args, **kwargs):
        if kwargs['password'] == 'qwerty12345':
            print('Access granted')
            func(*args)
        else:
            print('Access denied')
    return wrapper

@access
def send_message(mess):
    print(mess)

# send_message('Hesdfasdfasdfasdfllo', password='qwerty12345')

def up(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def warning(func):
    def wrapper(*args, **kwargs):
        return f'you have message:{func(*args, **kwargs)}'
    return wrapper

@warning
@up
def send_mess(mess):
    return(mess)


print(send_mess('hello'))