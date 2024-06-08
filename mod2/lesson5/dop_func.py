#enumerate
data = ['potates','onion','galik','oranges',
        'apples','eggs','meat','bananas','ananas','cucumber']

# for i in range(len(data)):
#     print(i+1,data[i])

# for num, elem in enumerate(data):
#     print(num+1,elem)
from itertools import zip_longest
#zip
data2 = [100,200,300,400,500,55,42,1000,2000,]
data3 = [2,3,4,5,6,7,8,9,10,11]
# for i in range(len(data)):
#     print(data[i],data2[i])

for elem, price, count in zip_longest(data,data2,data3):
    print(elem,price,count)