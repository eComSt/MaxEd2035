class Car:                         # создаем класс "Автомобиль”
         # описываем свойства класса
    mark = 'Toyota'                # марка
    model = 'Corolla'              # модель
    color = 'blue'                 # цвет
    speed = 0                      # скорость 
    def turn_on(self):              # метод
        print("Врум-м-м-м-м")
my_car_1 = Car()                   # создаем экземпляр класса Car
my_car_1.color = 'red'
my_car_2 = Car()
my_car_2.mark = 'BMW'

print(f'Марка автомобиля:{my_car_1.mark}')
print(f'Модель автомобиля:{my_car_1.model}')
print(f'Цвет автомобиля:{my_car_1.color}')
print(f'Текущая скорость:{my_car_1.speed}')

print(f'Марка автомобиля:{my_car_2.mark}')
print(f'Модель автомобиля:{my_car_2.model}')
print(f'Цвет автомобиля:{my_car_2.color}')
print(f'Текущая скорость:{my_car_2.speed}')