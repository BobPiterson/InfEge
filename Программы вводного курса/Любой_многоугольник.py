from turtle import *
delay(10)
penup()
goto(-180, -140)
pendown()
color('red', 'yellow')
begin_fill()
star = 170
five_star = 144
triangle = 120
square = 90
pentagon = 72
hexagon = 60
octagon = 45
XY = pos()
max = 360
left(36)
for i in range(max):
    forward(100 * 3)
    left(triangle)
    #print(i, '    ', XY[0], XY[1], pos()[0], pos()[1])
    if XY[0] == round(pos()[0]) and XY[1] == round(pos()[1]):
        #print('--- Выход по совпадению координат ---')
        break
end_fill()
done()