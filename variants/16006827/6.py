from turtle import *

k = 60

tracer(0)
left(90)

color('green')
begin_fill()
for i in range(4):
    forward(8 * k)
    right(90)
end_fill()

color('red')
begin_fill()
for i in range(3):
    forward(12 * k)
    right(120)
end_fill()

up()
color('black')
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)

done()

