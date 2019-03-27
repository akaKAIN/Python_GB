# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.
def diagnosis(name, surname, age, weigth, result):
    print('{} {}, {} год, вес {} - {}'.format(name, surname, age, weigth, result))


name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('How old are you?: '))
weigth = int(input('How much do you weigh?: '))

if 12 < age < 30 and 50 < weigth < 120:
    result = 'хорошее состояние'
    diagnosis(name, surname, age, weigth, result)
elif age > 30 and 50 > weigth < 120:
    result = 'следует заняться собой'
    diagnosis(name, surname, age, weigth, result)
elif age > 40 and 50 > weigth < 120:
    result = 'следует обратиться к врачу!'
    diagnosis(name, surname, age, weigth, result)
elif age < 12:
    print('Кто пустил ребенка??!')
elif age > 65:
    print('Займите очередь для пенсионеров.\n На этой неделе врач вероятно Вас посмотрит.')
else:
    result = 'Покиньте больницу, не расстраивайте больных!'
    diagnosis(name, surname, age, weigth, result)