import turtle

# задаем размер рабочего поля
os_x = 1500
os_y = 850
turtle.screensize(os_x, os_y)
turtle.pensize(10)
turtle.pencolor('red')
# рисуем рамку экрана
turtle.delay(10)
turtle.penup()
# передвигаем кисть в правый верхний угол экрана
turtle.goto(os_x // 2, os_y // 2)
turtle.pendown()
turtle.right(90)

for i in range(2):
    turtle.forward(os_y)
    turtle.right(90)
    turtle.forward(os_x)
    turtle.right(90)

turtle.exitonclick()