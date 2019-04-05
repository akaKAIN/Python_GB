import random

class Character:
    def __init__(self, name='Anonim', helth=100, damage=50, armor=1.2, motivation=1.0):
        self.name = name
        self.helth = helth
        self.damage = damage
        self.armor = armor
        self.motivation = motivation

    def to_attack(self, name_character):
        clear_damage = int(self.damage * (self.motivation - random.randint(0, 3) / 10) / name_character.armor)
        name_character.helth -= clear_damage
        print(f'{self.name} наносит урон {clear_damage}. '
              f'- Здоровье {name_character.name} опустилось до {name_character.helth}')

    def info(self):
        print(f'{self.name}')
        print('Здоровье:   {:^4}'.format(self.helth))
        print('Сила атаки: {:^4}'.format(self.damage))
        print('Броня:      {:^4}'.format(self.armor))
        print('Мотивация:  {:^4}\n'.format(self.motivation))




player = Character('', 120, 44, 1.2, 5.0)
enemy = Character("'Stone of Knowlege'", 1000, 24, 1.2, 1.0)
player.name = input('Введите имя бойца: ')

player.info()

while player.helth > 0 and enemy.helth > 0:
    if random.randint(1, 2) == 2:
        player.to_attack(enemy)
    else:
        enemy.to_attack(player)
else:
    if player.helth > 0:
        print('Славься {0}!!! Славься {0}!!!'.format(player.name))
    else:
        print('\nЭто трагедия для всей Вселенной...')
