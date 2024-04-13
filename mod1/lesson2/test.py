import random
from random import randint
a=randint(0,100)
b=randint(0,100)
score=0
print(a,"+",b,"=")
answer=int(input())
if answer==a+b:
    print("Верно")
    score=score+1
    while answer==a+b:
        a=randint(0,100)
        b= randint(0,100)
        print(a,"+",b,"=")
        52
        answer=int(input())
        if answer==a+b:
            print("Верно")
            score=score+1
        else:
            print("Неверно")
print("вы набрали балов:")
print(score)