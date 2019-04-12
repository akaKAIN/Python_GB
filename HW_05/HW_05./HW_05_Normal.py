import os
import shutil
from easy import move_to
from easy import move_up
from easy import look_a_round
from easy import create_dir
from easy import del_dir


"""Утилита навигации с функциями просмотра содержимого, создания, удаления директорий"""

adress = ''
menu_navigations = [
    'Перейти в директорию выше.', 'Перейти в указанную директорию',
    'Обобразить содержимое текущей директории', 'Вызвать меню с функционалом', 'Выход...'
]
menu_options = [
    'Отобразить содержимое текущей директории', 'Создать директорию (рекурсивно)',
    'Удалить директорию (рекурсивно) с указанием пути', 'Удалить директорию выбрав ее номер в списке',
    'вернуться назад'
]
# Удаляет переданный индекс в переданом списке
def del_dir_by_key(list):
    while True:
        try:
            index_del = int(input(f'* Введите номер удаляемой папки (0 - вернуться назад) > '))
        except ValueError as error:
            print(f'* {error} > Неверный ввод данных.\n')
            continue
        if index_del == 0:
            break
        for key, value in enumerate(list):
            if key == index_del - 1:
                shutil.rmtree(adress + value)
                print(f'* Папка {value} и ее содержимое, успешно удалены\n')


# Выводит меню навигации
def menu_navigation_print():
    for i in range(len(menu_navigations)):
        print(f'| {i + 1}. {menu_navigations[i]}')

# Принимает ввод пункта меню навигации, проверяет на правильность ввода int и передает дальше.
def input_answer_menu():
    while True:
        try:
            answer = int(input('Выберите пункт меню.\n >'))
            return answer
        except ValueError as error:
            print(f'{error}\n>Неверный ввод данных. Введите номер пункта меню.\n')
        menu_navigation_print()

# Меню функционала.
def menu_options_print():
    while True:

        print(f'*************************\n'
              f'* функциональное меню:')
        for i in range(len(menu_options)):
            print(f'* {i + 1}) {menu_options[i]}')
        print(f'*************************')
        try:
            answer = int(input(f'* выберите пункт\n* >'))
        except ValueError as error:
            print(f'* {error}\n* Невернный ввод данных.\n')
            continue

        if answer == 1:
            look_a_round(os.getcwd())
        elif answer == 2:
            adress = input('*  Создать директорию: >')
            create_dir(adress)
        elif answer == 3:
            adress = input('*  Удалить директорию: >')
            del_dir(adress)
        elif answer == 4:
            dirs, files = look_a_round(os.getcwd())
            del_dir_by_key(dirs)
        elif answer == 5:
            input('... нажмите Enter для выхода в меню навигации')
            break
        elif answer > 5 :
            print(f'* Неверный выбор пункта - выберите из предложенных.')

def menu_choise(answer):
    adress = os.getcwd()
    if answer == 1:
        adress = os.chdir((move_up(adress)))
        look_a_round(adress)
    elif answer == 2:
        adress = input('| Введите директорию для перехода >')
        adress = move_to(adress)
        look_a_round(adress)
    elif answer == 3:
        look_a_round(adress)
    elif answer == 4:
        menu_options_print()



print('''
Добро пожаловать в консоль управления.
Программа создана при поддержке ресурса GeekBrains.ru\n\n\n''')

while True:
    menu_navigation_print()
    answer = input_answer_menu()
    if answer == 5:
        print(f'... сеанс завершен ...')
        input()
        break
    elif 0 < answer <= 4:
        menu_choise(answer)
    else:
        print(f'Error >Введите номер из предложенного списка.\n')

