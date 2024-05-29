from pprint import pprint
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# d = {
#     'data':data,
#     'password':"qwerty123",
#     'login':'ecoms'
# }
# print(data[2][0])

# for line in data:
#     for i in line:
#         print(i)

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

summ = 0
for line in data:
    summ += sum(line)
print(summ)