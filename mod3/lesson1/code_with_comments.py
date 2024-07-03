# Модификаторы доступа в Python

# создаем класс для моделирования автомобиля
class Car:
    # инициализатор класс
    def __init__(self, color, model, speed=0):
        # публичное поле
        self.color = color
        # защищенное поле
        self._speed = speed
        # приватное поле
        self.__model = model

    # метод для вывода информации о полях на экран
    def show_info(self):
        print(f'Цвет:{self.color}')
        print(f'Текущая скорость:{self._speed}')
        print(f'Модель:{self.__model}')

# создаем объект класса Car
my_car = Car(color='Синий', speed=10, model='Skyline')
# вызываем метод show_info()
my_car.show_info()
# обращаемся к полю color
print(my_car.color)
# обращаемся к полю _speed
print(my_car._speed)
# обращаемся к полю __model
print(my_car.__model)
# меняем значение атрибута __model
my_car._Car__model = 'Solaris'
# обращаемся к полю __model через искажение имени
print(my_car._Car__model)

# -------------------------------------------------------

# Геттеры и сеттеры

# создаем класс для моделирования автомобиля
class Car:
    # инициализатор класс
    def __init__(self, color, model, speed=0):
        # публичное поле
        self.color = color
        # защищенное поле
        self._speed = speed
        # приватное поле
        self.__model = model

    # метод для вывода информации о полях на экран
    def show_info(self):
        print(f'Цвет:{self.color}')
        print(f'Текущая скорость:{self._speed}')
        print(f'Модель:{self.__model}')

    # геттер для получения значения __model
    def get_model(self):
        return self.__model
    
    # сеттер для обновления значения _speed
    def set_speed(self, new_speed):
        # проверка, что новое значение скорости больше нуля
        if new_speed > 0:
            self._speed = new_speed
        else:
            print('Скорость не может быть отрицательной!')

    # геттер для получения значения _speed
    def get_speed(self):
        return self._speed

# создаем объект класса Car
my_car = Car(color='Синий', speed=10, model='Skyline')
# вызываем сеттер для замены значения _speed на 100
my_car.set_speed(100)
# вызываем сеттер для замены значения _speed на -100
my_car.set_speed(-100)
# вызываем геттер для получения _speed
print(my_car.get_speed())
