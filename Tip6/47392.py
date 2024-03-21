from turtle import *

k = 30

tracer(0)
hideturtle()
seth(90)

# fillcolor('red')
# begin_fill()
for i in range(4):
    forward(12 * k)
    right(90)

# end_fill()
right(30)
fillcolor('blue')

begin_fill()
for i in range(3):
    forward(8 * k)
    right(60)
    forward(8 * k)
    right(120)

end_fill()
ans = 0

update()
canvas = getcanvas()

up()

b = 0
r = 0
k = 1
for x in range(0, 200):
    for y in range(-200, 0):
        h = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        # pencolor('black')
        # goto(x * k, -y * k)
        # dot(2)
        if h:
            # print(h, canvas.itemcget(h[-1], 'fill'))
            pencolor(canvas.itemcget(h[-1], 'fill'))
            # pencolor('black')
            goto(x * k, -y * k)
            dot(2)
            # r += int(canvas.itemcget(h[-1], 'fill') == 'red')
            # b += int(canvas.itemcget(h[-1], 'fill') == 'blue')

print(r, b, ans)
update()
print(1)
done()
