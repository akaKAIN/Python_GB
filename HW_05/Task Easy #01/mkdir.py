import os

count_dirs = int(input('Сколько папок желаете создать?\n'))
i = 0
plan = 0
while plan < count_dirs:
    i += 1
    try:
        os.mkdir('Directory#{:02}'.format(i))
        plan += 1
    except OSError:
        pass
