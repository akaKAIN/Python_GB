# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
user_name = input('Enter your name: ')
number = int(input('Enter a number: '))
float = float(input('Enter a real number: '))
list_ok = input('Enter list values, separated by a space. Press Enter for end: ').split()
print('{}, you are enter: \n1. number = {}\n2. real number = {}\n3. list = {}'
      .format(user_name, number, float, list_ok))


# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
number = int(input('Enter number: '))
print('You number ({}) + 2 = {}'.format(number, number + 2))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен"
# иначе "Извините, пользование данным ресурсом только с 18 лет"
user_age = int(input('How old are you?: '))
if user_age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')