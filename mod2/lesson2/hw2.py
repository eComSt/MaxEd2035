a = (1, 2, 3 , 4, 5, 6, 7, 8, 9) #числа в кортеже
n = int(input())
print('Ответ:',a[:n-1]+a[n:] if n in a else a)