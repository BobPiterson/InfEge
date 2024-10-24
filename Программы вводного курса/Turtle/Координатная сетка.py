import turtle
from math import sin, pi

turtle.dot(8)
# подписываем начало координат - "0"
turtle.penup()
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(20)
turtle.pendown()
turtle.write('0', font=("Arial", 14, "bold"))

# задаем размер рабочего поля
os_x = 1500
os_y = 800
turtle.screensize(os_x, os_y)
# рисуем рамку экрана
turtle.penup()
turtle.goto(os_x // 2,0)
turtle.setheading(0) 
turtle.pendown()
turtle.right(90)
for i in range(2):
    turtle.forward(os_y // 2)
    turtle.right(90)
    turtle.forward(os_x)
    turtle.right(90)
    turtle.forward(os_y // 2)

# рисуем ось Х
turtle.pensize(3) 
turtle.goto(- os_x // 2,0)
turtle.setheading(0) 
turtle.forward(os_x // 2)

# рисуем ось У
turtle.goto(0, - os_y // 2)
turtle.setheading(90) 
turtle.forward(os_y)
turtle.goto(0,0)

# рисуем функцию
t = 8 * pi / os_x # масштаб периода функции по оси х (растянутый на длину оси х)
h = 300 # масштаб значения функции по оси у
turtle.goto(- os_x // 2, 0)
for i in range(- os_x // 2, os_x // 2):
    turtle.goto(i, int(sin(i * t) * h))

turtle.exitonclick()