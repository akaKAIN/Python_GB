# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
equation = equation.replace(' ', '')
part1 = equation.split('=')                     # part1 = [y, -12x + 11111140.2121]
part2 = part1[1].split('+')                     # part2 = [-12x,  11111140.2121]
k = part2[0][:-1]
b = part2[1]
print(f'y = {int(k)} * {x} + {b} = {int(k) * x + float(b)}')


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

day_in_month = 30
day, month, year = input('Введите дату (в формате дд.мм.гггг): ').split('.')
if len(day) == 2 and len(month) == 2 and len(year) == 4:
    if 1 <= int(month) <= 12 and 1 <= int(year) <= 9999:
        if (int(month) <= 7 and int(month) % 2 != 0) or \
                (int(month) >= 8 and int(month) % 2 == 0):
            day_in_month = 31
    if 1 <= int(day) <= day_in_month:
        print('Дата введена корректно.')
    else:
        print('Введенные данные больше/меньше возможных.')
else:
    print('Введенные данные не соответствуют формату дд.мм.гггг')



# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)

room = int(input('Введите номер комнаты: '))
import math
# n - количество комнат в блоке
# last_room - последняя комната в блоке
# block_of_rooms - список комнат находящихся в блоке. Кол-во комнат в блоке х, = х ** 2
tower = [[1]]                   # Закладываем фундамент в виде первого этажа
last_room = 1
x = 1
max_block_floor = 1             # Счетчик блок-этажей. Каждый блок х занимает х этажей
# Построение БАШНИ!
while last_room < room:
    x += 1
    max_block_floor += x
    block_of_rooms = []         # Создаем каждый раз пустой блок (x) для заполнения
    turn = 0                    # Создаем нумератор комнат для блока, чтоб их было не более х ** 2
    while turn < x ** 2:
        turn += 1
        last_room += 1
        block_of_rooms.append(last_room)

    tower.append(block_of_rooms)


# Этаж начала блока.
floor_begin_of_last_block = max_block_floor - x
# Обрезаем последний блок до искомого номера квартиры
cut_block = block_of_rooms[:(block_of_rooms.index(room) + 1)]
result_floor = floor_begin_of_last_block + math.ceil(len(cut_block) / x)

# Костыль наверное, но времени уже не осталось.
# Чтобы вместо номеров кратным х не ставились нули.
if len(cut_block) % x == 0:
    result_num = x
else:
    result_num = len(cut_block) % x

print(f'Этаж: {result_floor},  номер двери: {result_num}')
