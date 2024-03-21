from turtle import *

k = 10
tracer(0)
color('red', 'red')
hideturtle()
begin_fill()
seth(90)
right(180)
fd(2 * k)
right(90)
fd(40 * k)
right(90)
fd(2 * k)
for i in range(4):
    seth(90)
    circle(-5 * k, 180)

end_fill()
sc = getcanvas()

update()
ans = 0

up()
color('green', 'red')
for x in range(-100 * k, 100 * k, k):
    for y in range(-100 * k, 100 * k, k):
        idx = sc.find_overlapping(x, y, x, y)
        if idx:
            if sc.itemcget(idx[-1], 'fill') == 'red':
                goto(x, -y)
                dot(4)
                ans += 1


print(ans)
done()
