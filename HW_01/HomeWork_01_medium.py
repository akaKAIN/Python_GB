# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
while True:
    num = input('Введите число х, где 0 < x < 10: ')
    if num.isdigit() is True:
        if 0 < int(num) < 10:
            print(int(num)**2)
            break
        else:
            print('Введенные данные не удовлетворяют условиям')
    else:
        print('Нужно ввести число ...')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
a = input('Enter number "а": ')
b = input('Enter number "b": ')
a, b = b, a
print('Now a = {}, and b = {}'.format(a,b))