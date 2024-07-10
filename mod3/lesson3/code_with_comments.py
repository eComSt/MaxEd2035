# Наследование

# Реализация наследования в Python

# Создаем класс для моделирования человека
class BaseHuman:
    # инициализатор класса
    def __init__(self, name, age):
        self.name = name    # имя
        self.age = age      # возраст
    
    # вывод информации об имени и возрасте
    def introduce(self):
        print(f'Привет, меня зовут {self.name}!')
        print(f'Мой возраст: {self.age}')


# Создаем класс для моделирования программиста
# Наследуемся от класса BaseHuman
class Programmer(BaseHuman):
    pass
 
human = BaseHuman(name='Миша', age=25)      # экземпляр класса BaseHuman
proger = Programmer(name='Дима', age=26)    # экземпляр класса Programmer
# вызовы метода introduce()
human.introduce()
proger.introduce()
# вывод на экран локальных свойств объектов
print(human.__dict__)
print(proger.__dict__)

# ---------------------------------------------------------------------------------

# Переопределение атрибутов и функция super()

# Создаем класс для меделирования человека
class BaseHuman:
    # инициализатор класса
    def __init__(self, name, age):
        self.name = name    # имя
        self.age = age      # возраст
    
    # вывод информацию об имени и возрасте
    def introduce(self):
        print(f'Привет, меня зовут {self.name}!')
        print(f'Мой возраст: {self.age}')

# Создаем класс для моделирования программиста (итоговая версия)
# Наследуемся от класса BaseHuman
class Programmer(BaseHuman):
    # инициализатор класса
    def __init__(self, name, age, language):
        # вызываем метод __init__() из базового класса
        super().__init__(name, age)        
        self.language = language    # язык программирования

    def coding(self):
        print(f'Программист {self.name} сейчас пишет код!')


human = BaseHuman(name='Миша', age=25)                         # экземпляр класса BaseHuman
proger = Programmer(name='Дима', age=26, language='Python')    # экземпляр класса Programmer
proger.coding()     # вызов метода coding() для объекта proger
human.coding()      # вызов метода coding() для объекта human (ошибка)
print(proger.__dict__)  # выводим на экран локальные свойства объекта proger

# ----------------------------------------------------------------------------------------

# Многоуровневое наследование

# Создаем класс для меделирования человека (итоговая версия)
class BaseHuman:
    # инициализатор класса
    def __init__(self, name, age):
        self.name = name    # имя
        self.age = age      # возраст
    
    # вывод информацию об имени и возрасте
    def introduce(self):
        print(f'Привет, меня зовут {self.name}!')
        print(f'Мой возраст: {self.age}')
    
    # информирование, что человек идет на прогулку
    def walk(self):
        print(f'{self.name} идет на прогулку.')


# Создаем класс для моделирования программиста (итоговая версия)
# Наследуемся от класса BaseHuman
class Programmer(BaseHuman):
    # инициализатор класса
    def __init__(self, name, age, language):
        # вызываем метод __init__() из базового класса
        super().__init__(name, age)        
        self.language = language    # язык программирования

    def coding(self):
        print(f'Программист {self.name} сейчас пишет код!')


class BackendProgrammer(Programmer):
    pass

# экземпляр класса BackendProgrammer
backproger = BackendProgrammer(name='Иван', age=27, language='C++')
# выводим на экран локальные свойства объект backproger
print(backproger.__dict__)
# вызов метода walk() для объекта backproger
backproger.walk()

# ---------------------------------------------------------------------------------

# Функции issubclass() и isinstance()

# Весь дальнейший код пишется с учетом наличия в коде классов BaseHuman, Programmer и BackendProgrammer

# проверяем, что класс BackendProgrammer является подклассом для Programmer
print(issubclass(BackendProgrammer, Programmer))
# проверяем, что класс BackendProgrammer является подклассом для BaseHuman
print(issubclass(BackendProgrammer, BaseHuman))
# выводим на экран базовый класс для класса Programmer
print(Programmer.__base__)
# выводим на экран базовый класс для класса BaseHuman
print(BaseHuman.__base__)
# проверяем, что классы Programmer и BackendProgrammer являются подклассами для object
print(issubclass(Programmer, object))
print(issubclass(BackendProgrammer, object))
# проверяем, что proger является экземпляром класса Programmer
print(isinstance(proger, Programmer))
# проверяем, что proger является экземпляром класса BaseHuman
print(isinstance(proger, BaseHuman))
