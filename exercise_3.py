import turtle
import math
a = 100
turtle.penup()
turtle.forward(a)
turtle.pendown()
turtle.left (90)
for i in range (360):
    x = 2 * a * math.cos(i) - a * math.cos(2 * i)
    y = 2 * a * math.sin(i) - a * math.sin(2 * i)
    turtle.goto(x,y)




