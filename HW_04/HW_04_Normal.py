# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате:
#  - текст в нижнем регистре,
#  - допускается нижнее подчеркивание и цифры,
#  - потом @,
#  - потом текст,
#  - допускаются цифры,
#  - точка,
#  - ru или org или com.
#
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re

# Шаблоны регулярных выражений для проверки валидности в функциях
regex_name = (r'^[A-Z|А-Я][a-z|а-я]+$')
regex_email = (r'^[a-z0-9_]+@[a-z0-9]+\.(ru|org|com)$')

menu_options = ['Поочередный ввод данных, с поочередной проверкой.',
                'Поочередный ввод данных с проверкой всего блока в конце.',
                'Ввод данных одной строкой через пробел и проверка.',
                '..Выход\n']
base_name = [False, False]
base_surname = [False, False]
base_email = [False, False]


# Функция проверки валидности имени/фамилии/email.
def valid_check(text, pattern, name=None):
    if text != '':
            name = input(f'{text}: ')
    match_text = re.match(pattern, name)
    return [name, match_text is not None]



# Опция меню №1
def option1(name, surname, email):
    while name[1] is False:
        name = valid_check('Введите имя с заглавной буквы', regex_name)
        if name[1] is not True:
            print('Введенное имя не соответствует нужному формату,\n'
                  '\t\t-попробуйте еще раз')

    while surname[1] is False:
        surname = valid_check('Введите фамилию с заглавной буквы', regex_name)
        if surname[1] is not True:
            print('Введенная фамилия не соответствует нужному формату,\n'
                  '\t\t-попробуйте еще раз')

    while email[1] is False:
        email = valid_check('Введите адрес электронной почты в нижнем регистре: ', regex_email)
        if email[1] is not True:
            print('Формат почты не корректен.\n'
                  '\t\t-попробуйте еще раз')
    return [name, surname, email]

def option2():
    while True:
        i = 3                       # счетчик выхода
        valid_array = []            # Массив хранящий в себе данные о валидности введенных данных
        name = valid_check('Введите имя с заглавной буквы', regex_name)
        valid_array.append(name)
        surname = valid_check('Введите фамилию с заглавной буквы', regex_name)
        valid_array.append(surname)
        email = valid_check('Введите адрес электронной почты в нижнем регистре: ', regex_email)
        valid_array.append(email)
        for check in valid_array:
            if check[1] is not True:
                print(f'Вы неверно ввели свои данные - {check[0]}')
                i -= 1
        if i == 3:
            return valid_array

def option3():
    while True:
        i = 3                       # счетчик выхода
        valid_array = []            # Массив хранящий в себе данные о валидности введенных данных
        name, surname, email = input('Введите через пробел свои имя, фамилию и адрес электронной почты.\n'
                                     'Имя и фамилию с заглавной буквы, а почту в нижнем регистре: ').split()
        name = valid_check('', regex_name, name)
        valid_array.append(name)
        surname = valid_check('', regex_name, surname)
        valid_array.append(surname)
        email = valid_check('', regex_email, email)
        valid_array.append(email)
        for check in valid_array:
            if check[1] is not True:
                print(f'Вы неверно ввели свои данные - {check[0]}')
                i -= 1
        if i == 3:
            return valid_array


for num, option in enumerate(menu_options, start=1):
    print(f'{num}. {option}')

choise = int(input('Выберите один из пунктов выше: '))
print()


if choise == 1:
    user_info = option1(base_name, base_surname, base_email)
elif choise == 2:
    user_info = option2()
elif choise == 3:
    user_info = option3()
elif choise == 4:
    print('\nGood look!')

print(f'Ваше имя: {user_info[0][0]}, Ваша фамилия: {user_info[1 ][0]}, и почта: {user_info[2][0]}')
print('Все введено правильно.')











# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

import re
pattern = (r'\.\.')
if re.search(pattern, some_str) is not None:
    print('В тексте обнаружены более двух точек подрят')
else:
    print('В тексте нет более одной точки подряд')