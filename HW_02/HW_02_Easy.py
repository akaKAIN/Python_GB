# ----------- Task #1
fructs = ["яблоко", "банан", "киви", "арбуз"]
for i in range(len(fructs)):
    print('{}. {:>6}'.format(i + 1, fructs[i]))


# ----------- Task #2
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_numbers1 = [1,2,3,4,5,6,7,8]
list_numbers2 = [1,6,7,8,9,0]
for number in list_numbers1[::-1]:
    if number in list_numbers2:
        list_numbers1.pop(list_numbers1.index(number))
print(list_numbers1)



# ----------- Task #3
# Дан произвольный список из целых чисел (#numbers)
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
numbers = [1,2,3,4,5,6,7,8,9]

# Первый вариант:
result_list = []
for number in numbers:
    if number % 2 == 0:
        result_list.append(number / 4)
    else:
        result_list.append((number * 2))
print(f'Result_1 ={result_list}')

# Второй вариант
result_list = [number / 4 if number % 2 == 0 else number * 2 for number in numbers]
print(f'Result_2 ={result_list}')