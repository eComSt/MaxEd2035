from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacchi(n-1) + fibonacchi(n-2)
    
