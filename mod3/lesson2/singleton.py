class Captain:
    __cap = None
    def __new__(cls, *args, **kwargs):
        if not cls.__cap:
            cls.__cap = super().__new__(cls)
        return cls.__cap
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def show_info(self):
        print(self.name, self.age, self.height, self.weight)

cap  = Captain('Andrey', 25, 1.75, 65)
cap2 = Captain('Ilya', 23, 1.8, 70)
cap2.age = 99
cap.show_info()