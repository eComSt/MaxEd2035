# def hash(f):
#     dct = {}
#     def wrapper(n):
#         if n not in dct:
#             dct[n] = f(n)
#         return dct[n]
#     return wrapper



# @hash
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1)+fib(n-2)
from time import time
t = time()
print(fib(499))
print(time()-t)