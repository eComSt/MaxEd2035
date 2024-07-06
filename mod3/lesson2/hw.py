class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def __repr__(self):
        return f'BankAccount(balance={self.__balance})'
    def __add__(self, other):
        if  isinstance(other, (float,int)):
            return BankAccount(self.__balance + other)
        print("Некорректное пополнение счета")
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if  isinstance(other, (float,int)):
            if self.__balance - other < 0:
                print("Баланс не может стать отрицательным!")
            else:
                return BankAccount(self.__balance - other)
        else:
            print("Некорректное списание средств со счета")
my_acc = BankAccount(10000)
my_acc = my_acc + 1000.123
print(my_acc)
my_acc = 200 + my_acc
print(my_acc)
my_acc = my_acc - 5000
print(my_acc)
my_acc = my_acc - 10000
print(my_acc)