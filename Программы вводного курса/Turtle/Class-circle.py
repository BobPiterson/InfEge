import turtle
from random import randint, randrange, choice

turtle.colormode(255)
turtle.delay(0)
for i in range(100):
    circle = turtle.Turtle()
    circle.hideturtle() 
    circle.penup()
    circle.goto(randrange(-600, 600), randrange(-400, 400))
    circle.pendown()
    circle.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    circle.begin_fill()
    r = randrange(36, 56)
    circle.circle(r)
    circle.end_fill()

    # установка указателя и подпись номера
    circle.penup()
    circle.left(90)
    circle.forward(r // 2)
    circle.left(90)
    circle.forward(r // 4)
    circle.pendown()
    circle.write(i, font=("Arial", r // 2, "bold"))

turtle.exitonclick()