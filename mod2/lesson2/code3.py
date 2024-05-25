import sys

objects_list = []
print(sys.getsizeof(objects_list))    # получаем 56

objects_list = [1]    
print(sys.getsizeof(objects_list))    # получаем 64

objects_list = [1, 2]
print(sys.getsizeof(objects_list))    # получаем 72

objects_tuple = tuple()
print(sys.getsizeof(objects_tuple))   # получаем 40

objects_tuple = (1,)
print(sys.getsizeof(objects_tuple))   # получаем 48

objects_tuple = (1, 2)
print(sys.getsizeof(objects_tuple))   # получаем 56 (разница в 16 байт)

objects_list = []
for num in range(10000):
    objects_list.append(num)
print(sys.getsizeof(objects_list))    # получаем 85176

objects_tuple = tuple(objects_list)
print(sys.getsizeof(objects_tuple))   # получаем 80040 (разница в 5176 байт)