from turtle import *

k = 50

tracer(0)
left(90)

fillcolor('green')
begin_fill()
for i in range(4):
    forward(9 * k)
    right(90)
end_fill()

fillcolor('red')
begin_fill()
for i in range(3):
    forward(9 * k)
    right(120)
end_fill()

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5)

done()
