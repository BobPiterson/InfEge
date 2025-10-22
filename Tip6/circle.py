import turtle
turtle.delay(0) # ускорить выполнение
k = 50 # коэффициент масштабирования

# Рисуем систему координат
turtle.forward(10 * k)
turtle.right(180)
turtle.forward(2 * 10 * k)
turtle.goto(0, 0)
turtle.right(90)
turtle.forward(10 * k)
turtle.right(180)
turtle.forward(2 * 10 * k)
turtle.goto(0, 0)
turtle.dot(20)
turtle.seth(0) # устанавливаем абсолютное направление: вправо по Х

# рисование дуги радиуса r на a градусов
turtle.delay(10)
r = 120 # Если радиус с минусом, рисование дуги будет по часовой стрелке, если с плюсом - Против
a = 90 # угол
turtle.penup() # поднять кисть
turtle.forward(r)
turtle.pendown() # опустить кисть
turtle.left(90)  # повернем голову вверх
turtle.circle(r, a) # рисуем против часовой стрелке на угол а
turtle.circle(-r, 3* a) # рисуем по часовой стрелки на угол а
turtle.circle(r, a) # рисуем против часовой стрелке на угол а
turtle.circle(-r, 3* a) # рисуем по часовой стрелки на угол а

turtle.exitonclick() # не закрывать окно, пока не сделал по нему клик мышкой