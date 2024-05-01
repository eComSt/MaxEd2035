def f(x=3):
    return x**2
# x = 6
# y = f(x)
# print(y) ctrl+/
def show_info(lst):
    print(lst)
    print(type(lst))
    print(f"Count: {len(lst)}")
    print(f"Sum: {sum(lst)}")
    print(f"Max: {max(lst)}")
    print(f"Min: {min(lst)}")
    print(f"Average: {sum(lst)/len(lst)}")

numbers = [1,2,3,4,5,42,52]
show_info(numbers)
numbers.append(100)
show_info(numbers)



