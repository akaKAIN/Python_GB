print(
	'''Приветствую!
	Вы попали на ДЗ второго урока Python.
	Давайте познакомимся''')
name = input('Как Ваше имя?  ')
answer = input('Рад видеть Вас, {} желаете закоммитить ченить,  Y/N?  '.format(name))
if answer.lower() == 'y':
	print('Excellent! Ни дня без кода!')
else:
	print('Жаль ... теряешь время')