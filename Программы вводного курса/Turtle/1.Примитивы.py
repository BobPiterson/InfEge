import turtle

# задаем размер рабочего поля
os_x = 1500
os_y = 850
turtle.screensize(os_x, os_y)
#
turtle.pensize(5)

# Квадрат
turtle.pencolor('blue')
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)

# треугольник
turtle.pencolor('red')
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

# шестиугольник
turtle.pencolor('green')
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.left(60)

turtle.exitonclick()
