import abc

def area(figure):
    return figure.get_area()
def perimetr(figure):
    return figure.get_perimetr()

class Figure(abc.ABC):
    @abc.abstractmethod
    def get_area(self):pass
    @abc.abstractmethod
    def get_perimetr(self):pass
    def get_info(self):
        return f'Площадь: {self.get_area()}, Периметр: {self.get_perimetr()}'