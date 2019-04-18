import os
from random import randint
from random import sample

class Card:
    def __init__(self, name):
        self.name = name
        self.card = self._generate_card_num
        self.format_card = self._generating_card_rows

    # Создает 3 вложенных списка с 5ю неповторяющимися номерами в каждом (от 1 до 90])
    @property
    def _generate_card_num(self):
        card = []
        while not card or len(set([num for row in card for num in row])) != 15:
            card = []
            while len(card) != 3:
                row = sample(
                    [randint(1, 9), randint(10, 19), randint(20, 29),
                     randint(30, 39), randint(40, 49), randint(50, 59),
                     randint(60, 69), randint(70, 79), randint(80, 90)], 5)
                card.append(row)
        return card

    # Распределяет 15 цифр из списков в те места, где они должы стоять на "карточках" лото
    @property
    def _generating_card_rows(self):
        format_card = []
        for row in self.card:
            row.sort()
            format_row = ['  ' for i in range(9)]
            for num in row:
                try:
                    format_row[num // 10] = num
                except IndexError:
                    format_row[8] = num
            format_card.append(format_row)
        return format_card


    def check_number(self, num):
        for row in self.format_card:
            if num in row:
                return self.name
        return False

    @property
    def look_who_win(self):
        for row_num in self.format_card:
            if row_num.count(' -') == 5:
                return self.name
        return False
    
class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy
        self.numbers_in_bug = [num for num in range(1, 91)]
        self.winner = None

    # Отрисовка карточек игроков.
    def draw_cards(self):

        # Очистка экрана.
        def clear_screen():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        # Вывод имени владельца карточки.
        def draw_card_of(name):
            print('{}{}{}'.format(
                '=' * ((26 - len(name)) // 2),
                name,
                '=' * ((26 - len(name)) // 2))
            )

        # Вывод оставшихся номеров на карточке игрока.
        def draw_card_lines(lines):
            for row_nums in lines:
                print('{: >2} {} {} {} {} {} {} {} {}'.format(
                    row_nums[0], row_nums[1], row_nums[2], row_nums[3], row_nums[4],
                    row_nums[5], row_nums[6], row_nums[7], row_nums[8])
                )
            print('=' * 26)

        # Тело выполнения функции (отрисовки).
        clear_screen()
        draw_card_of(self._player.name)
        draw_card_lines(self._player.format_card)
        draw_card_of(self._enemy.name)
        draw_card_lines(self._enemy.format_card)

    def taking_number(self):
        num = sample(self.numbers_in_bug, 1)[0]
        print(f'numbers in bug = {self.numbers_in_bug}')
        print(f'taking number = {num}')
        self.numbers_in_bug.remove(num)
        print(f'count in bag = {len(self.numbers_in_bug)}')
        return num

    def cross_out_number(self, num):
        for row_num in self._player.format_card:
            if num in row_num:
                answer = input(f'\n'
                               f'Желаете зачеркнуть цифру {num}?\n'
                               f'"Y"-зачеркнуть и продолжить'
                               f'"N"-просто продолжить\n'
                               f'что выберете?--->  ')
                if answer.lower() == ('y' or 'yes' or 'да'):
                    row_num[row_num.index(num)] = ' -'

    def cross_out_number_by_default(self, num):
        for row_num in self._enemy.format_card:
            if num in row_num:
                row_num[row_num.index(num)] = ' -'

    def start(self):
        while not self._player.look_who_win and not self._enemy.look_who_win:
            new_number = self.taking_number()
            self.draw_cards()
            print(f'\nВыпало число {new_number}')
            if self._player.check_number(new_number):
                self.cross_out_number(new_number)
            if self._enemy.check_number(new_number):
                self.cross_out_number_by_default(new_number)
            input('\n... нажмите Enter для продолжения.\n\n')
        if self._player.look_who_win:
            winner_name = self._player.look_who_win
        else:
            winner_name = self._enemy.look_who_win
        print('STOP the GAME! we have a winner!')
        print(f'\n<<Удача на стороне игрока {winner_name}>>')
        input('\n\nEnter - закончить игру.')


print('''
    Добро пожаловать в игру "ЛОТО"

Правила игры:
1. Номера выпадают автоматически.
2. Компьютер зачеркивает выпадающие номера автоматически
3. Вы должны подтверидить зачеркивание номера в своей карточке, иначе
   этот номер не зачеркнется и Вы уменьшите свои шансы на победу.
4. Первый зачеркнувший номера в одном своем ряду - побеждает.

    Желаю Вам удачи!
    ''')
player = Card(input('Введите ваще имя: '))
comp = Card('Computer')

new_game = Game(player, comp)

new_game.start()