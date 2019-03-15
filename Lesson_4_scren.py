import turtle
import random



def coondinate(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def screen_drow(x, y, r):
    turtle.fillcolor(random.random(), random.random(), random.random())
    turtle.begin_fill()
    coondinate(x, y)
    turtle.circle(r)
    turtle.end_fill()


k = 10
j = 0
number = int(turtle.textinput('Screen', 'Сколько кругов?'))

for i in range(number):
    screen_drow(random.randrange(-600, 600),random.randrange(-500, 200), ((number * k) - j))
    j += k
input()