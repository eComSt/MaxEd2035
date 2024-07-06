class MoneyBox:

    def __init__(self, money = 0):
        self.__money = money

    def __repr__(self):
        return f'MoneyBox({self.__money})'
    
    def __str__(self):
        return str(self.__money)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money + other)
        elif isinstance(other, MoneyBox):
            return MoneyBox(self.__money + other.__money)
        else:
            return "Wrong type"
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money - other)
        elif isinstance(other, MoneyBox):
            return MoneyBox(self.__money - other.__money)
        else:
            return "Wrong type"
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money * other)    
        else:
            return "Wrong type"
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money / other)
        else:
            return "Wrong type"
        
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money // other)
        else:
            return "Wrong type"
    def __rfloordiv__(self, other):
        return self.__floordiv__(other)
    
    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money % other)
        else:
            return "Wrong type"
    def __rmod__(self, other):
        return self.__mod__(other)
    
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money ** other)
        else:
            return "Wrong type"
        
    def __rpow__(self, other):
        return self.__pow__(other)
    
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.__money == other
        elif isinstance(other, MoneyBox):
            return self.__money == other.__money
        else:
            return "Wrong type"
    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.__money!= other
        elif isinstance(other, MoneyBox):
            return self.__money!= other.__money
        else:
            return "Wrong type"
    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.__money > other
        elif isinstance(other, MoneyBox):
            return self.__money > other.__money
        else:
            return "Wrong type"
    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.__money >= other
        elif isinstance(other, MoneyBox):
            return self.__money >= other.__money
        else:
            return "Wrong type"
    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.__money < other
        elif isinstance(other, MoneyBox):
            return self.__money < other.__money
        else:
            return "Wrong type"
    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.__money <= other
        elif isinstance(other, MoneyBox):
            return self.__money <= other.__money
        else:
            return "Wrong type"
    def __int__(self):
        return int(self.__money)
    
box = MoneyBox(100)
print(int(box))