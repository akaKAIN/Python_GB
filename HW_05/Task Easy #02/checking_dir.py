import os
import random


menu_list = ['создать случайное число папок', 'посмотреть содержимое', 'удалить все папки', 'выход.']
simvol = 'qwertyuiopasdfghjklzxcvbnm0987654321'

def name_generator(length_word):
    name = ''
    for i in range(length_word):
        name += simvol[random.randrange(len(simvol))]
    return name

while True:
    print('|----------------------------\n|Выберите пункт меню:')
    for key, value in enumerate(menu_list, start=1):
        print(f'| {key}. {value}')
    choise = input('|----------------------------\n|> ')

    if choise == '1':
        for i in range(random.randint(2, 50)):
            try:
                os.mkdir(f'{name_generator(random.randint(10,20))}')
            except OSError:
                continue

    elif choise == '2':
        for element in os.listdir():
            print(f'{element}')
        input('... нажмите Enter для продолжения.\n\n')

    elif choise == '3':
        for element in os.listdir():
            if os.path.isdir(element):
                os.rmdir(element)
        print('Все папки удалены.')
        input('... нажмите Enter для продолжения.\n\n')

    elif choise == '4':
        break