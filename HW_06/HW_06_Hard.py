# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

import random


class ToyFactory:
    def __init__(self, name=None, color=None, toy_type=None):
        self.name = name
        self.color = color
        self.toy_type = toy_type
        self.purchase()
        self.craft()
        self.painting()
        self.__label

    def purchase(self):
        print(f'Закупка сырья для игрушки')

    def craft(self):
        self.toy_type = random.choice(toys_types)
        print(f'Взятие схемы выкройки {self.toy_type}a и его пошив')

    def painting(self):
        self.color = random.choice(toys_color)
        print(f'Покраска будущей игрушки в {self.color} цвет')
        self.name = random.choice(toys_names)

    @property
    def __label(self):
        return print(f'Игрушка "{self.color} {self.toy_type} по имени {self.name}" - ГоТоВа.')


class Toy(ToyFactory):
    def __init__(self):
        super().__init__(ToyFactory)







toys_types = [
    'охотник', 'волк', 'пингвин', 'крот',
    'мутант', 'Питон', 'носорог', 'тигр'
]
toys_names = [
    'Элвин', 'Свистун', 'Ходор', 'Луи',
    'Хьюго', 'Шуршун', 'Дэйв', 'Иван'
]
toys_color = [
    'желтый', 'синий', 'черный', 'белый',
    'красный', 'лиловый в желтую крапинку',
    'прозрачный', 'мутный', 'сизый'
]

toy1 = ToyPython()
print(toy1.toy_type)
