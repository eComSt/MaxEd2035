# Конструкторы и параметр self

# Методы класса, параметр self

# создаем класс Car
class Car:
    # описываем свойства класса
    mark = 'Toyota'     # марка
    model = 'Corolla'   # модель
    color = 'blue'      # цвет
    speed = 0           # скорость

    # метод для создания нового свойства - power_engine
    def set_power_engine(self, power_engine):
        self.power_engine = power_engine

    # метод для вывода информации о свойствах класса
    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self.speed}')

    # метод для возвращения значений свойств класса
    def get_params(self):
        return (self.mark, self.model, self.color, self.speed)

# создаем два экземпляра класса Car
my_car_1 = Car()
my_car_2 = Car()
# вызываем метод set_power_engine() непосредственно для класса Car
Car.set_power_engine()
# вызываем метод set_power_engine() непосредственно для объекта my_car_1
Car.set_power_engine(my_car_1)
# вызываем метод set_power_engine() для объекта my_car_1 с аргументом 200
my_car_1.set_power_engine(200)
# выводим на экран значение свойства power_engine
print(f'Мощность двигателя: {my_car_1.power_engine}')

# выводим на экран локальные атрибуты для объектов my_car_1 и my_car_2
print(my_car_2.__dict__)
print(my_car_1.__dict__)
# выводим на экран локальные атрибуты класса Car
print(Car.__dict__)

# вызываем метод show_info() для объекта my_car_2
my_car_2.show_info()

# получаем значения свойств объекта my_car_1 и сохраняем в кортеж params_car_1
params_car_1 = my_car_1.get_params()
print(params_car_1)

# ----------------------------------------------------------

# Инициализатор и финализатор объектов класса

# создаем класс Car
class Car:

    # инициализатор класса
    def __init__(self, mark='', model='', color='', speed=0):
        self.mark = mark    # марка
        self.model = model  # модель
        self.color = color  # цвет
        self.speed = speed  # скорость
    
    # финализатор класса
    def __del__(self):
        print('Сработал метод __del__')

    # метод для создания нового свойства - power_engine
    def set_power_engine(self, power_engine):
        self.power_engine = power_engine
    
    # метод для вывода информации о свойствах класса
    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self.speed}')

    # метод для возвращения значений свойств класса
    def get_params(self):
        return (self.mark, self.model, self.color, self.speed)

# создаем экземпляр класса Car
my_car_1 = Car()
# выводим на экран локальные атрибуты объекта my_car_1
print(my_car_1.__dict__)

# создаем экземпляр класса Car c заданными параметрами
my_car_1 = Car('Nissan', 'Juke', 'red', 0)
# выводим на экран значения всех свойств объекта my_car_1
print(my_car_1.get_params())

# создаем экземпляр класса Ca
my_car_2 = Car()
# выводим на экран значения всех свойств объекта my_car_2
print(my_car_2.get_params())

# создаем два экземпляра класса Car для демонстрации работы финализатора
my_car_1 = Car('Nissan', 'Juke', 'red', 0)
my_car_2 = Car()

# ----------------------------------------------------------

# Герои меча и магии

# создаем класса Hero
class Hero:
    # инициализатор класса
    def __init__(self, name, health, damage, defense):
        self.name = name        # имя
        self.health = health    # здоровье
        self.damage = damage    # наносимый урон
        self.defense = defense  # защита

    # получаем статус параметров героя
    def get_status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье:{self.health}')
        print(f'Урон: {self.damage}')
        print(f'Защита:{self.defense}')
        print('--------------------------------------------------')

    # метод увеличения защиты героя
    def increase_defense(self):
        # если значение защиты меньше 100
        if self.defense * 1.5 < 100:
            # увеличение защиты в 1.5 раза
            self.defense *= 1.5
        else:
            print('Достигнут максимальный уровень защиты!')
        print(f'Текущий уровень защиты: {self.defense}')
        print('--------------------------------------------------')

    # метод нанесения урона по врагу
    def make_damage(self, enemy):
        print(f'Атака по персонажу {enemy.name}!')
        print('--------------------------------------------------')
        # вызываем метод get_damage() у вражеского героя
        enemy.get_damage(self.damage)
        
    # метод получения урона, учитывая защиту
    def get_damage(self, damage):
        # формула поглощенного урона: урон * защита / 100
        absorbed_damage = damage * self.defense / 100
        # вычисление финального урона
        final_damage = damage - absorbed_damage
        print(f'По герою {self.name} нанесли урон {final_damage}!')
        # уменьшение здоровья героя
        self.health -= final_damage
        print('--------------------------------------------------')

# создаем два экземпляра класса Hero
hero_1 = Hero('Артур', 100, 20, 5)
hero_2 = Hero('Робин', 80, 30, 4)

# получаем статус о параметрах Артура 
hero_1.get_status()
# увеличиваем защиту Артура
hero_1.increase_defense()

# получаем статус о параметрах Робина 
hero_2.get_status()
# Робин наносит урон Артуру
hero_2.make_damage(hero_1)

# получаем статус о параметрах Артура  
hero_1.get_status()
