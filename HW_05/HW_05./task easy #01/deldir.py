import os


dir_elements = os.listdir()
agry_list = ['y', 'yes', 'д', 'да', 'давай', 'погнали', 'хорошо', 'можно', 'ок']
negativ_list = ['нет', 'ненадо', 'н', 'неа', 'n', 'nope', 'no', 'never', 'nine']

# Функция удаления директорий по переданному списку директорий
def rm_all_dirs(list):
    [os.rmdir(dir) for dir in list]
    print('Все директории удалены')

#Проверка на число папок.
dirs_list = []
count_dirs = 0

print('Папки:')
for element in dir_elements:
    if os.path.isdir(element):
        count_dirs += 1
        print(f'{count_dirs}. {element}')
        dirs_list.append(element)
print(f'Обнаружено папок - {count_dirs}')

if count_dirs > 0:
    answer = input('Желаете их удалить? (Y/N)\n')
    if answer.lower() in agry_list:
        rm_all_dirs(dirs_list)
    elif answer.lower() in negativ_list:
        print('Ну чтож, пусть тогда пылятся')
    else:
        print('Очевидно вы не отдаете сее отчет в том, что делаете.\n'
              'Скрипт берет на себя всю ответственность, отдохните.')
        rm_all_dirs(dirs_list)
else:
    print('Удалять нечего, программа закрывается ...')
    input()