from time import time
def decorator(f):
    def wrapper(*args, **kwargs):
        try:
            ans = f(*args, **kwargs)
        except:
            print("error")
            return False
        return ans
    return wrapper

def timeit(f):
    def wrapper(*args, **kwargs):
        t = time()
        ans = f(*args, **kwargs)
        print(f"time taken: {time()-t}")
        return ans
    return wrapper

@timeit
@decorator
def func(x,y):
    return x/y

print(func(3,0))