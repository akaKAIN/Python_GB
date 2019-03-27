import turtle
import random
import math


# Функция отрыва и перемещения "пера"
def coordinate(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Функция рисования рандомной пули.
def random_bullet(hole, color):
    coordinate(math.sin(angle * hole) * (r), math.cos(angle * hole) * (r) + 75)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()


# Радиус
r = 70
turtle.speed(0)
turtle.circle(100)
coordinate(0, 200)
turtle.circle(5)
answer = ''
start = 0


angle = (360 / 7)*math.pi/180
for i in range(7):
    coordinate(math.sin(angle * i) * (r), math.cos(angle * i) * (r) + 75)
    turtle.circle(25)

while answer.lower() == '':
    answer = turtle.textinput('Хотите сыграть?.', 'Enter - Yes\n N - No')
    if answer.lower() == '':
        for i in range(start, random.randint(7, 36)):
            coordinate(math.sin(angle * i) * (r), math.cos(angle * i) * (r) + 75)
            turtle.circle(25)
            random_bullet(i, "red")
            random_bullet(i, "white")
    random_bullet(i, "red")
    start = i % 7
    if start == 0:
        coordinate(-50, 250)
        turtle.write("Вы проиграли", font=("Arial", 18, "normal"))
        break





