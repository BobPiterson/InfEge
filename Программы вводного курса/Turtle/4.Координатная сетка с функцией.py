import turtle
from math import sin, pi, factorial
turtle.delay(0)
#turtle.speed(12)
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
os_y = 850
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

turtle.goto(- os_x // 2, 0)
turtle.pensize(5)

# рисуем функцию y = sin(x)
t = 4 * pi / os_x # масштаб периода функции по оси х (растянутый на длину оси х)    t = 0.00837
h = 300 # масштаб значения функции по оси у

turtle.pencolor('red')
turtle.penup() # поднимаем кисть, если надо рисовать точками. Если рисуем отрезками, кисть не поднимаем.
for x in range(- os_x // 2, os_x // 2 + 1):
    turtle.goto(x, int(sin(x * t) * h))
    turtle.dot(3)

# функция y = kx + b
k = 0.8
b = -100

turtle.pencolor('blue')
turtle.penup() # поднимаем кисть, если надо рисовать точками. Если рисуем отрезками, кисть не поднимаем.
for x in range(- os_x // 2, os_x // 2 + 1):
    turtle.goto(x, int(k * x + b))
    # if int(k * x + b) > -os_y // 2 and  int(k * x + b) < os_y // 2: 
    #     turtle.dot(3)


# функция y = a * x ** 2 + b * x + c
a = 0.01
b = - 2
c = -300
turtle.pencolor('indianred')
turtle.penup() # поднимаем кисть, если надо рисовать точками. Если рисуем отрезками, кисть не поднимаем.
for x in range(- os_x // 2, os_x // 2 + 1):
    turtle.goto(x, int(a * x ** 2 + b * x + c))
    #if int(a * x ** 2 + b * x + c) > -os_y // 2 and  int(a * x ** 2 + b * x + c) < os_y // 2: 
        #turtle.dot(3)

# рисуем функцию y = sin(x) через ряд Тейлора
# t = 4 * pi / os_x # масштаб периода функции по оси х (растянутый на длину оси х)    t = 0.00837
# h = 300 # масштаб значения функции по оси у
# m = 7 # количество членов ряда
# turtle.pencolor('green')
# turtle.penup() # поднимаем кисть, если надо рисовать точками. Если рисуем отрезками, кисть не поднимаем.
# for x in range(- os_x // 2, os_x // 2 + 1):
#     summa = 0
#     for i in range(1, m + 1):
#         summa += ((-1) ** (i - 1) * (x * t) ** (2 * i - 1) / factorial(2 * i - 1))
#     turtle.goto(x, int(summa * h))
#     turtle.dot(3)


turtle.exitonclick()