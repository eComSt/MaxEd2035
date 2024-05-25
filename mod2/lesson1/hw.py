# На вход с клавиатуры подаются два натуральных числа — N и M, 
# каждое в отдельной строке. После чего генерируются два списка, 
# в одном содержится N чисел, в другом M чисел.
# Элементы списков генерируются случайным образом, в диапазоне от 1 до 100.
# Программа должна посчитать и вывести на экран количество чисел, 
# которые содержатся одновременно как в первом списке, так и во втором.
from random import randint
N,M = int(input()), int(input())
N_list, M_list = [] ,[]
for _ in range(N): N_list.append(randint(1,100))
for _ in range(M): M_list.append(randint(1,100))
N_set, M_set = set(N_list), set(M_list)
ans = N_set.intersection(M_set)
print(len(ans))
