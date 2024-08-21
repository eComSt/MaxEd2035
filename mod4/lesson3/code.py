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

func()