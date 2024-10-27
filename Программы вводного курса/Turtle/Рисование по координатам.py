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

# рисование ласточки
# (-5, 4), (-7, 4), (-9, 6), (-11, 6), (-12, 5), (-14, 5), (-12, 4), (-14, 3), (-12, 3), 
# (-11, 2), (-10, 2), (-9, 1), (-9, 0), (-8, -2), (0,-3), (3, -2), (19, -2), (4, 0), 
# (19, 4), (4, 2), (2, 3), (6, 9), (10, 11), (3, 11), (1, 10), (-5, 4), глаз (-10.5, 4.5).

turtle.penup()
turtle.goto(-50, 40)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('black')

turtle.goto(-70, 40)
turtle.goto(-90, 60)
turtle.goto(-110, 60) 
turtle.goto(-120, 50) 
turtle.goto(-140, 50) 
turtle.goto(-120, 40) 
turtle.goto(-140, 30) 
turtle.goto(-120, 30) 
turtle.goto(-110, 20) 
turtle.goto(-100, 20) 
turtle.goto(-90, 10) 
turtle.goto(-90, 0) 
turtle.goto(-80, -20) 
turtle.goto(00,-30) 
turtle.goto(30, -20) 
turtle.goto(190, -20) 
turtle.goto(40, 0) 
turtle.goto(190, 40) 
turtle.goto(40, 20) 
turtle.goto(20, 30) 
turtle.goto(60, 90) 
turtle.goto(100, 110) 
turtle.goto(30, 110) 
turtle.goto(10, 100) 
turtle.goto(-50, 40) 
#глаз 
turtle.penup()
turtle.goto(-105, 45)
turtle.pendown()
turtle.dot(10)

turtle.exitonclick()