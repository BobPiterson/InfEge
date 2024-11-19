from turtle import *
# углы различных многоугольников
star = 170
star2 = 175
star3 = 145
five_star = 144
triangle = 120
square = 90
pentagon = 72
hexagon = 60
octagon = 45

delay(0)
# ширина пера
width(2)
# цвет пера и цвет закраски
color('red', 'yellow')
penup()
goto(-60, -250)
pendown()

begin_fill()
# сохраним координаты пера в списке
XY = pos()
# Зададим максимальное количество повторений цикла
max = 360
left(36)
for i in range(max):
    forward(100 * 3)
    # Развернуть против часовой стрелки на указанный угол
    left(star3)
    #Если координаты пера повторились, т.е. фигура прорисована, выходим из цикла
    if XY[0] == round(pos()[0]) and XY[1] == round(pos()[1]):
        #print('--- Выход по совпадению координат ---')
        break
end_fill()
exitonclick()