import os
import shutil

def move_to(adress):
    try:
        os.chdir(adress)
        print(f'| Вы перемещены по адресу >{adress}')
    except FileNotFoundError as error:
        print(f'| {error}\n| >Имя располодения директории задано не верно.\n')
        return os.getcwd()
    return adress

def move_up(adress):
    up_adress = os.path.split(adress)[0]
    print(f'| Вы перешли в директорию >{up_adress}')
    return up_adress

def look_a_round(adress):
    print(f'| Содержимое  {adress}:\n'
          f'|----------------------------------------------')
    dir_list = os.listdir()
    files = []
    dirs = []
    for element in dir_list:
        if os.path.isdir(element):
            dirs.append(element)
        elif os.path.isfile(element):
            files.append(element)
    files.sort()
    dirs.sort()
    if len(dirs) > 0:
        print(f'| Папки:')
        for index, dir in enumerate(dirs, start=1):
            print(f'|   {index}. {dir}')

    if len(files) > 0:
        print(f'| Файлы:')
        for index, file in enumerate(files, start=1):
            print(f'|   {index}. {file}')
    print(f'|----------------------------------------------')
    return dirs, files

def del_dir(adress):
    if os.path.isdir(adress):
        confirm = input('| Вы уверены. что хотите удалить папку {}\n'
                        '| и ее содержимое? (Y/N)\n'
                        '| >'.format(adress))
        if confirm.lower() == 'y' or confirm.lower() == 'yes':
            shutil.rmtree(adress)
            print(f'| Папка {adress} и ее содержимое, успешно удалены.')
    else:
        print('Error >По указанному адресу, директория не найдена.')

def create_dir(adress):
    try:
        print(os.getcwd())
        os.makedirs(adress)
        print('| Конечная директория создана.')
    except FileExistsError as error:
        print(f'| {error}\n| >Директория с таким именем уже существует.')
    except FileNotFoundError as error:
        print(f'| {error}\n| >Пользователь ничего не ввел.')

