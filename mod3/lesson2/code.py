class Car:

    def __new__(cls, *args, **kwargs):
        # print(f"working method __new__ of {cls} class")
        # print(f"args: {args}")
        # print(f"kwargs: {kwargs}")
        return super().__new__(cls)
    
    def __init__(self, color,model,speed):
        self.color = color
        self.model = model
        self.speed = speed
    
    def __str__(self):
        return f"color: {self.color}, model: {self.model}, speed: {self.speed}"

    def __repr__(self):
        return f"Car({self.color}, {self.model}, {self.speed})"

my_car = Car("red","bmw",200)
print(my_car)
print(repr(my_car))