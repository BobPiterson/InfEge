from turtle import *
print(pos())
delay(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200 * 2)
    left(170)
    #print(pos())
    if abs(pos()) < 1:
        #print(abs(pos()))
        break
end_fill()
done()