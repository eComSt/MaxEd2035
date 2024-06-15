class Car:   # создаем класс Car
    def __init__(self,mark = "BMW",model = "X3",color="red",speed=0):
        self.mark = mark   # марка
        self.model = model # модель
        self.color = color    # цвет
        self.speed = speed         # скорость
         # метод для создания нового свойства - power_engine

    def __del__(self):
        print('Уничтожено')
    
    def set_power_engine(self,power_engine):
        if type(power_engine) == int:
            if power_engine > 0 and power_engine < 10000:
                self.power_engine  = power_engine
            else:
                print('Неверный значение')
        else:
            print('Неверный тип данных')

    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self.speed}')

    def __str__(self):
        return f'Марка: {self.mark} Модель: {self.model} Цвет: {self.color} Текущая скорость: {self.speed}'

    def get_params(self):
        return self.mark, self.model, self.color, self.speed

my_car_1 = Car()
print(my_car_1)    
print(my_car_1.__dict__)
my_car_1 = 1
# my_car_2 = Car()
# my_car_1.set_power_engine(-100)
# my_car_2.mark = 'BMW'
# Car.color = 'green'
# print(my_car_2.color)
# print(my_car_2.__dict__)                                                      
# my_car_1.speed = 100
# # Car.set_power_engine(my_car_1)
# my_car_1.set_power_engine(200)
# # print(my_car_1.power_engine)
# my_car_1.show_info()
# my_car_2.show_info()
# data = my_car_1.get_params()
# mark, model, color, speed = data
# print(mark, model, color, speed)
