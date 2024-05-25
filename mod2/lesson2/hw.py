number = int(input())
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
if number in t:
    index = t.index(number)
    t = t[:index] + t[index+1:]
print(t)