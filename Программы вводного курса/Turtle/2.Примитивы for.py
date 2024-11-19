import turtle

# задаем размер рабочего поля
os_x = 1500
os_y = 850
turtle.screensize(os_x, os_y)
#
turtle.pensize(5)
turtle.dot(10)

# Квадрат
turtle.pencolor('blue')
for i in range(4):
    turtle.forward(200)
    turtle.left(90)

# треугольник
turtle.pencolor('red')
for i in range(4):
    turtle.forward(200)
    turtle.left(120)

# шестиугольник
turtle.pencolor('green')
for i in range(6):
    turtle.forward(200)
    turtle.left(60)

turtle.exitonclick()
