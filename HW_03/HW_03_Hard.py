# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.



# player = dict(name='', helth=120, damage=350)
# enemy = dict(name='Granite sience', helth=1000, damage=50)
# player['name'] = input('Enter your name, warrior: ')
#
# def attack(person1, person2):
#     person2['helth'] -= person1['damage']
#     print('{}, нанес {} урона.\n\tYровень здоровья {} упал до {}.'\
#           .format(person1['name'], person1['damage'], person2['name'], person2['helth'] ))
#     if person2['helth'] < 0:
#         print('{} повержен!!!!\n Слава победителю - '.format(person2['name'], person1['name']))
#
#
# attack(player, enemy)





# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random

player = dict(name='Kain', helth=150, damage=60, armor=1.2, motivation=5.0)
enemy = dict(name='-Гранит науки-', helth=1000, damage=30, armor=1.2, motivation=1.0)
#player['name'] = input('Enter your name, warrior: ')

def armor_check(person1, person2):
    clear_damage = person1['damage'] * person1['motivation']/ person2['armor']
    return int(clear_damage)

def attack(person1, person2):
    person2['helth'] -= armor_check(person1, person2)
    print('{}, нанес {} урона.\n\tYровень здоровья {} упал до {}.\n\n'\
          .format(person1['name'], armor_check(person1, person2), person2['name'], person2['helth'] ))
    if person2['helth'] <= 0:
        print('{} повержен!!!!\n Слава победителю - '.format(person2['name'], person1['name']))


while (player['helth'] or enemy['helth']) > 0:
    dise_num = random.randint(1,2)
    if dise_num % 2 == 0:
        attack(player, enemy)
    else:
        attack(enemy, player)


