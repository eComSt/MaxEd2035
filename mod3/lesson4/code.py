import sys
from  figures import Rectangle, Triangle, Circle
# Создание экземпляра класса Rectangle
r1 = Rectangle(5, 10)
r2 = Rectangle(2, 4)
t1 = Triangle(5, 6, 6)
t2 = Triangle(10, 10, 10)
c1 = Circle(5)
c2 = Circle(10)
figures = [r1, r2, t1, t2, c1, c2]
for i in figures:
    print(i._name, i.get_info())
    print(sys.getsizeof(i))