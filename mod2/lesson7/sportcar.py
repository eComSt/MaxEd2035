from classes import SportCar

cars = []
for _ in range(3):
    car = SportCar()
    car.mark = input('Введите марку:')
    car.model = input('Введите модель:')
    car.power = int(input('Введите мощность двигателя:'))
    car.max_speed = int(input('Введите макс. скорость:'))
    cars.append(car)
    print('---------------------------')

print('Машины в автопарке:') 
for car in cars:
    print(car.mark, car.model, car.power, car.max_speed)
    print('---------------------------')