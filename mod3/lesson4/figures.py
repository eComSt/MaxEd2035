from fig import Figure
    
class Rectangle(Figure):
    def __init__(self, length, width):
        self._name = 'Прямоугольник'
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width
    
    def get_perimetr(self):
        return 2 * (self._length + self._width)

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self._name = 'Треугольник'
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def get_area(self):
        p = self.get_perimetr()/2
        return (p*(p-self._side1)*(p-self._side2)*(p-self._side3))**0.5
       
    def get_perimetr(self):
        return self._side1 + self._side2 + self._side3
    
class Circle(Figure):
    def __init__(self, radius):
        self._name = 'Круг'
        self._radius = radius

    def get_area(self):
        return 3.14 * self._radius**2
    
    def get_perimetr(self):
        return 2 * 3.14 * self._radius