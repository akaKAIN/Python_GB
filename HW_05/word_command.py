# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.


import os
import sys
import shutil


def help_menu():
    print('"cp" - Make a file copy')
    print('"rm" - deliting file')
    print('"cd" - move to directory')
    print('"com" - вызов основного интерфейса')


def copy_file():
    if not item_name:
        print('* Имя файла не задано')
        return
    for i in range(100):
        if f'{i:02}-copy_' + item_name not in os.listdir():
            shutil.copy(item_name, f'{i:02}-copy_' + item_name)
            print('* Копия файла успешно создана')
            break


def del_file():
    try:
        os.remove(item_name)
        print(f'* Файл {item_name} успешно удален.')
    except FileNotFoundError as error:
        print(f'* {error}\n* >Объект не найден (не существует)')


def move_to_dir():
    try:
        os.chdir(item_name)
        show_path()
    except FileNotFoundError as error:
        print(f'* {error}\n* >Директория не найдена (не существует)')



def show_path():
    print(f'Вы находитесь: {os.getcwd()}')

# Пытался в основной утилите вызвать скрипт, содержащий словарь команд и sys.argv, но не смог
# реализовать передачу аргументов при импорте.
# Поэтому зашел с обратной стороны.
def load_main_script():
    import HW_05_Normal


commands = dict(help=help_menu,
                cp=copy_file,       # param1 = <file name>              |>Создает копию указанного файла
                rm=del_file,        # param1 = <file name>              |>Удаляет указанный файл с подтверждением
                cd=move_to_dir,     # param1 = <full or relative path>  |>Меняет текущую директорию на указанную
                ls=show_path,        # param1 = <full path>             |>Отображает полный путь текущей директории
                com=load_main_script    # загрузка основного скрипта
                )

# Проверка наличия второго параметра (имени файла или директории)
try:
    item_name = sys.argv[2]
except IndexError as error:
    item_name = None

# Проверка введенного ключа на наличие такого в словаре команд
key = sys.argv[1]
if key:
    if commands.get(key):   # Возвращает значение ключа, или None, если ключа нет в словаре (блок else)
        commands[key]()
    else:
        print(f'* Команды {key} не сушествует.\n'
              f'* Наберите "help", чтобы посмотреть список доступных команд')


