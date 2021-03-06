# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name=None, health=100, damage=15, armor=1.2):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    @property
    def info(self):
        print(f'Name:  {self.name}\n'
              f'Health: {self.health}\n')
        return

    def _clear_damage(self, other):
        cl_damage = int((self.damage + random.randrange(-5, 5)) / other.armor)
        return cl_damage

    def attack(self, other):
        cl_damage = self._clear_damage(other)
        print(f'{self.name} наносит {other.name} целых {cl_damage} ед. урона')
        other.health -= cl_damage
        print(f'Здоровье несчастного опустилось до {other.health}\n')

class Player(Person):
    def __init__(self, name, damage=15, health=120, armor=1.5):
        super().__init__(Person)
        self.name = name
        self.armor = armor
        self.damage = damage
        self.health = health

class Enemy(Person):
    def __init__(self, name='Enemy', damage=20, health=100):
        super().__init__(Person)
        self.name = name
        self.damage = damage
        self.health = health


enemy = Enemy()
player = Player('Player')
# print(f'player.health={player.health}, enemy.health={enemy.health}')

while enemy.health > 0 and player.health > 0:
    if random.randrange(1, 3) % 2 == 0:
        player.attack(enemy)
    else:
        enemy.attack(player)

print(f'Битва завершилась победой {player.name if player.health >= 0 else enemy.name}')
player.info
enemy.info
