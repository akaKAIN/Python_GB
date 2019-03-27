print(
	'''Приветствую!
	Вы попали на ДЗ второго урока Python.
	Давайте познакомимся''')
name = input('Как Ваше имя?  ')
answer = input('Рад видеть Вас, {} желаете закоммитить ченить,  Y/N?  '.format(name))
if answer.lower() == 'y':
	print('Excellent! Ни дня без кода!')
	choise = input(
		'''Введите номер пункта меню для выбора:
		1. Запустить Python
		2. Запустить диспетчер задач
		3. Запустить командную строку
		4. Уйти за кофем\n''')
	if choise == '1':
		print('Запускаем Python ...\n\n')
		input()
	elif choise == '2':
		print('Диспетчер в пути ...\n\n')
		input()
	elif choise == '3':
		print('Ищем командную строку\n\n')
		input()
	elif choise == '4':
		print('Кофе пьем, коды бьем!\n\n')
		input()
	else:
		print('Я Вас опять не понимаю.\n\n')

elif answer.lower() == 'n':
	print('Жаль ... теряешь время')
else:
	print('Что-то? ...')