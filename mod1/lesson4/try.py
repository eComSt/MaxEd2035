x = 2**18
for i in range(x-1,1,-1):
    y = x
    while y>=i: y = y - i
    if y==0:
        print(i)
        break
else:
    print("Делителя нет")