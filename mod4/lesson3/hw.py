def is_even_sum(f):
    def wrapper(*args):
        return True if f(*args) % 2 == 0 else False
    return wrapper

@is_even_sum
def get_sum(*args):
    return sum(args)

print(get_sum(1,2,3,4))