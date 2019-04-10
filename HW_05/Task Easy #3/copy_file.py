import os
import shutil


elements_list = os.listdir()
elements_list.sort()
script_info = os.path.split(os.path.realpath(__file__))

for i in range(len(elements_list)):
    print(f'| {i + 1}. {elements_list[i]}')
try:
    answer = int(input('|---------------------------------------------------------\n'
                       '| Выберите в меню пункт с файлом, который хотите скопировать.\n'
                       '| (0 - скопировать файл запущенного скрипта)\n| > '))
    if answer == 0:
        shutil.copy(script_info[1], 'copy-' + script_info[1])
    else:
        shutil.copy(elements_list[answer - 1], 'copy--' + elements_list[answer - 1])

    print(f' Файл --> {elements_list[answer - 1]} скопирован.')
except IndexError:
    print('Остановка скрипта - выбран не существующий пункт')
except ValueError:
    print('Остановка скрипта - некорректный выбор пункта')