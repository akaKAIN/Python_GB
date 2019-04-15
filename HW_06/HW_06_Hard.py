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

# Сперва нужно создать родительский класс Игрушка с атрибутами имя и цвет.
# Создать несколько дочерних классов ИгрушкаТип с унаследованными атрибутами
# имя и цвет и атрибутом тип по умолчанию. Далее основной действующий
# класс ToyFactory, с методом создания игрушки. Т.е. он принимает название
# игрушки, цвет, тип и в зависимости от типа создает экземпляр соответствующего
# класса ИгрушкаТип (животное, солдатики, машинки, куклы ....)

import random


toys_types = [
    'охотник', 'волк', 'опосум', 'котейка',
    'мутант', 'Питон', 'носорог', 'тигр'
]
toys_names = [
    'Элвин', 'Свистун', 'Ходор', 'Шпуньк',
    'Хьюго', 'Шуршун', 'Арнольд', 'Иван'
]
toys_color = [
    'желтый', 'синий', 'черный', 'белый',
    'красный', 'хмурый', 'одинокий',
    'прозрачный', 'мутный', 'сизый'
]
soft_toys = [
    'плюшевый медвепут', 'плюшевый Гейб',
    'плюшевый змей', 'плюшевый огурец'
]
person_toys = [
    'капитан', 'царь', 'учитель', 'плут', 'дурачок'
]


class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    @property
    def label(self):
        return print(f'\nПеред Вами игрушка:\n{self.color} {self.toy_type} по имени {self.name}')


class SoftToy(Toy):
    def __init__(self, name, color, toy_type=random.choice(soft_toys)):
        Toy.__init__(self, name, color, toy_type)
        self.toy_type = toy_type

class PersonToy(Toy):
    def __init__(self, name, color, toy_type=random.choice(person_toys)):
        Toy.__init__(self, name, color, toy_type)
        self.toy_type = toy_type



class ToyFactory(Toy):
    def __init__(self,
                 name=random.choice(toys_names),
                 color=random.choice(toys_color),
                 toy_type=random.choice(toys_types)
                 ):
        Toy.__init__(self, name, color, toy_type)
        self.name = name
        self.color = color
        self.toy_type = toy_type
        self.__purchase
        self.__crafting
        self.__painting

    def make_soft_toy(self):
        return SoftToy(self.name, self.color)

    def make_person_toy(self):
        return PersonToy(self.name, self.color)


    @property
    def __purchase(self):
        return print('Закупаем материал')

    @property
    def __crafting(self):
        return print('Изготвливаем игрушку по шаблону')

    @property
    def __painting(self):
        return print('Окрашиваем игрушку')


crafting_toy = ToyFactory()
crafting_toy.label

a = crafting_toy.make_soft_toy()
a.label

b = crafting_toy.make_person_toy()
b.label