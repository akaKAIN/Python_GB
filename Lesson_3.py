


import os
import sys
import psutil

print(
	'''Приветствую!
	Вы попали на ДЗ второго урока Python.
	Давайте познакомимся''')
name = input('Как Ваше имя?  ')
answer = input('Рад видеть Вас, {} желаете закоммитить ченить,  Y/N?  '.format(name))
if answer.lower() == 'y':
	print('Excellent! Ни дня без кода!')
	while True:
		choise = input(
		'''Введите номер пункта меню для выбора:
		1. Просмотреть файлы в директории
		2. Посмотреть версию ОС, и др.
		3. Запустить командную строку
		4. Уйти за кофем\n''')

		if choise == '1':
			d = input('Введите адрес директории или нажмите Enter,\nчтобы просмотреть текущую: ')
			if d == '':
				os.chdir(r'C:\Users\mkain\OneDrive\Documents\Git\Python_GB')
				print(os.listdir())
			else:
				for i in os.listdir(d):
					print(i)

		elif choise == '2':
			ver, a1, bild, a2, a3 = sys.getwindowsversion()
			print('Windows {}, сборка-{}'.format(ver, bild))
			print('Python: ', sys.version)
			print('Число ядер проц-ра: ' + str(psutil.cpu_count()))
			print('Частота процессора: ' + str(psutil.cpu_freq()))
			print('Загрузка процессора: ' + str(psutil.cpu_percent())+ '%\n')

		elif choise == '3':
			os.startfile(r'C:\Windows\System32\cmd.exe')

		elif choise == '4':
			print('Кофе пьем, коды бьем!\nУвидимся позже!')
			break

		else:
			print('Я Вас опять не понимаю.\n\n')


elif answer.lower() == 'n':
	print('Жаль ... теряешь время')
else:
	print('Что-то? ...')
	