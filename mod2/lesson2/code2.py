# def func(a, b, c):
#     print(a, b, c)

# objects_tuple = (1, 2, 3)
# func(objects_tuple[0],objects_tuple[1],objects_tuple[2])
# func(*objects_tuple)
# func(1,2,3)

def func(a, b, c):
    summa = a + b + c
    diff = a - b - c
    return summa, diff

ans = func(1,2,3)
print(ans,type(ans))
# s,d = func(1,2,4)
# print(s,d)

# t = (1,2,3)
# if not t:
#     print('Empty')
# else:
#     print('Not Empty')
# a,b = (42,14)
# t = (42,)
# print(t,type(t))
# lst = [1, 2, 3]
# tuple_with_lists = (lst, [4, 5, 6])
# lst.append(42)
# print(tuple_with_lists)