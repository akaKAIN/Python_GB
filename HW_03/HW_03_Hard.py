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



player = dict(name='', helth=120, damage=350)
enemy = dict(name='Granite sience', helth=1000, damage=50)
player['name'] = input('Enter your name, warrior: ')

def attack(person1, person2):
    person2['helth'] -= person1['damage']
    print('{}, нанес {} урона.\n\tYровень здоровья {} упал до {}.'\
          .format(person1['name'], person1['damage'], person2['name'], person2['helth'] ))
    if person2['helth'] < 0:
        print('{} повержен!!!!\n Слава победителю - '.format(person2['name'], person1['name']))


attack(player, enemy)





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
import os
os.chdir('/home/kain/Git/Python_GB/HW_03/')

# Функция открывает файл по заданному адресу
# и заполняет из него переданный словарь.
# Возвращает словарь
def character_loading(dict, adress_name_file):
    with open(adress_name_file, encoding='utf-8') as character_file:
        for line in character_file:
            key, value = line.split()
            try:                                        # обход ошибки присвоения значения float строковому значению
                dict[key] = float(value)                # в нашем случае - это name игрока
            except ValueError:
                dict[key] = value
    return dict

# Функция расчитывает чистый урон за вычетом параметров брони обороняющегося
# и с прибавкой мотивации атакующего.
def armor_check(person1, person2):
    clear_damage = person1['damage'] * person1['motivation']/ person2['armor']
    return int(clear_damage)


# Функция производит "нанесение урона" и вывод имени победителя, в случае смерти
def attack(person1, person2):
    person2['helth'] -= armor_check(person1, person2)
    print('{}, нанес {} урона.\n\tYровень здоровья {} упал до {}.\n\n'\
          .format(person1['name'], armor_check(person1, person2), person2['name'], person2['helth'] ))
    if person2['helth'] <= 0:
        print('{} повержен!!!!\n Слава победителю - {}'.format(person2['name'], person1['name']))


# Создаем пустые словари, чтобы было куда записывать данные с файлов.
player = {}
enemy = {}

# Заполняем словари из файлов.
character_loading(player, 'player.txt')
player['name'] = input('Enter your name, warrior: ')            # ввод имени игрока
character_loading(enemy, 'enemy.txt')

# Цикл боя, противники наносят друг другу удары в случайном порядке.
while (player['helth'] and enemy['helth']) > 0:
    dise_num = random.randint(1,2)
    if dise_num % 2 == 0:
        attack(player, enemy)
    else:
        attack(enemy, player)


