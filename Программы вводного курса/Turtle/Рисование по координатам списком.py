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

# --------------------------------- рисование ласточки ---------------------------------------
# xy = ((-5, 4), (-7, 4), (-9, 6), (-11, 6), (-12, 5), (-14, 5), (-12, 4), (-14, 3), (-12, 3), \
# (-11, 2), (-10, 2), (-9, 1), (-9, 0), (-8, -2), (0,-3), (3, -2), (19, -2), (4, 0),  \
# (19, 4), (4, 2), (2, 3), (6, 9), (10, 11), (3, 11), (1, 10), (-5, 4))

# pict = list(map(lambda val: (val[0] * 10, val[1] * 10), xy))
# turtle.penup()
# turtle.goto(pict[0])
# turtle.pendown()
# turtle.pensize(5)
# turtle.pencolor('black')

# for i in range(1, len(pict)):
#     turtle.goto(pict[i])
# #глаз 
# turtle.penup()
# turtle.goto(-105, 45)
# turtle.pendown()
# turtle.dot(10)
# -----------------------------------------------------------

# --------------------------------- рисование верблюда ---------------------------------------
# xy = ((-10, -2), (-11, -3), (-10.5, -5), (-11, -7), (-12, -10), (-11, -13), (-13, -13), (-13.5, -7.5), (-13, -7), (-12.5, -5), \
#     (-13,-3), (-14,-1), (-14, 4), (-15, -6), (-15, -3), (-14, 2), (-11, 4), (-10, 8), (-8, 9), (-6, 8), (-5, 5), (-3,8), (-1,9), \
#     (0,8), (0.5,6), (0.5,4), (3,2.5), (4,3), (5,4), (6,6), (8,7), (9.5,7), (10,6), (11.5,5.5), \
#     (12,5), (12,4.5), (11,5), (12,4), (11,4), (10,3.5), (10.5,1.5), (10,0), (6,-3), (2,-5), (1.5,-7), (1.5,-11), (2.5,-13), (1,-13), \
#     (0,-5), (-0.5,-11), (0,-13), (-1.5,-13), (-1.5,-7), (-2,-5), (-3,-4), (-5,-4.5), (-7,4.5), (-9,-5), (-10,-6), (-9,-12), (-8.5,-13), \
#     (-10.5,-13), (-10,-9.5), (-11,-7))
# #    глаз (8.5,5.5))
# scale = 30
# pict = list(map(lambda val: (val[0] * scale, val[1] * scale), xy))
# turtle.penup()
# turtle.goto(pict[0])
# turtle.pendown()
# turtle.pensize(5)
# turtle.pencolor('black')

# for i in range(1, len(pict)):
#     turtle.goto(pict[i])
# #глаз 
# turtle.penup()
# turtle.goto(8.5 * scale, 5.5 * scale)
# turtle.pendown()
# turtle.dot(10)
# -----------------------------------------------------------

# --------------------------------- рисование утки ---------------------------------------
xy = ((3, 0), (1, 2), (-1, 2), (3, 5), (1, 8), (-3, 7), (-5, 8), (-3, 4), (-6, 3), (-3, 3), (-5, 2),(-5, -2), (-2, -3), \
    (-4, -4), (1, -4), (3,-3), (6, 1), (3, 0))
# глаз (-1, 5)

scale = 30
pict = list(map(lambda val: (val[0] * scale, val[1] * scale), xy))
turtle.penup()
turtle.goto(pict[0])
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('black')

for i in range(1, len(pict)):
    turtle.goto(pict[i])

# #глаз 
turtle.penup()
turtle.goto(-1 * scale, 5 * scale)
turtle.pendown()
turtle.dot(10)

# -----------------------------------------------------------


turtle.exitonclick()