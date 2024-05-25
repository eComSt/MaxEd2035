object_tuple = tuple()
object_tuple = (1, 2, 3, 4, 5, 6)
st = "Hello, world!"
lst = [1,2,3]
o_tuple = tuple(lst)
# o_tuple[1] = 42
# print(object_tuple, type(object_tuple))

object_tuple = (1, 2, 3, 4, 5, 6, 2, 3, 4,2,3,2,3,2,3,2)
# first = object_tuple[0]
# second = object_tuple[1]
# third = object_tuple[2]
first, second, third = object_tuple[:3]
# print(first,second,third)
# for i in object_tuple:
    # print(i)
# print(object_tuple.count(2))
# print(object_tuple.index(5))
first_tuple = (1, 2 ,3)
second_tuple = (3, 4, 5)
# ctrl+/
third_tuple =second_tuple[1:] + first_tuple[:2] + second_tuple[1:2]
print(third_tuple)
# 4,5,1,2,4