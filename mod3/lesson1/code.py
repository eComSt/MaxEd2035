class Car: #создаем класс для моделирования автомобиля
    def __init__(self, color, model, speed=0): #инициализатор класс
        self.color = color #публичное поле
        self._speed = speed #защищенное поле
        self.__model = model #приватное поле
    def get_model(self): #метод для получения значения приватного поля
        if self._speed<100:
            return self.__model
        else:
            return "Не разглядел"
    def get_speed(self): #метод для записи значения в защищенное поле
        return self._speed
    def set_speed(self, speed): #метод для записи значения в защищенное поле
        if speed<0:
            print('Ни шагу назад!')
        elif speed>200:
            print('Не так быстро!')
            self._speed = 200
        else:
            self._speed = speed
    def show_info(self): #метод для вывода информации о полях на экран
        print(f'Цвет:{self.color}')
        print(f'Текущая скорость:{self._speed}')
        print(f'Модель:{self.__model}')
my_car = Car(color='Синий', speed=100, model='Skyline')#создаем объект класса Car

# my_car._speed = 100 #записываем значение в защищенное поле
# my_car.show_info() #вызываем метод show_info()
model = my_car.get_model() #вызываем метод get_model()
print(model)
my_car.set_speed(-100) #записываем значение в защищенное поле
print(my_car.get_speed()) #вызываем метод get_speed()