class BaseHuman:
    def __init__(self, name, age, pol):
        self.name = name
        self.age = age
        self.pol = pol

    def introduce(self):
        print(f'My name is {self.name} and I am {self.age} years old.')

    def walk(self):
        print(f'{self.name} is walking now!')

class Programmer(BaseHuman):
    def __init__(self, name, age, pol,language):
        super().__init__(name, age,pol)
        # BaseHuman.__init__(self, name, age)
        self.language = language

    def coding(self):
        print(f'{self.name} is writing code now!')

    def walk(self):
        print(f'Programmers do not walk')

class BackEndProgrammer(Programmer):    
    pass

# human = BaseHuman('John', 25)
proger = Programmer('Misha', 36, "Python","M")
be = BackEndProgrammer('Misha', 36, 'M',"Python")
be.walk()
# print(issubclass(BackEndProgrammer, Programmer))
print(BackEndProgrammer.__base__.__base__.__base__.__base__)
print(issubclass(BackEndProgrammer, object))
print(isinstance(proger, Programmer))
print(isinstance(proger, BaseHuman))