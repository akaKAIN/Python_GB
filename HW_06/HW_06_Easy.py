# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name=None, speed=60, color='White', is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    @property
    def info(self):
        return print(f'модель: {self.name}\n'
                     f'скорость: {self.speed}\n'
                     f'цвет: {self.color}\n'
                     f'служебная: {self.is_police}\n')

    def go(self):
        return print(f'Машина {self.name} поехала')

    def stop(self):
        return print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

class TownCar(Car):
    def __init__(self, name):
        super().__init__(name)

class SportCar(Car):
    def __init__(self, name):
        super().__init__(name, speed=290, color='Red')

class WorkCar(Car):
    def __init__(self, name):
        super().__init__(name, speed=90, color='Gray')

class PoliceCar(Car):
    def __init__(self, name):
        super().__init__(name, speed=120, color='Blue', is_police=True)



my_car = WorkCar('Ford')
my_car.info
my_car.go()
my_car.stop()
my_car.turn('направо')

