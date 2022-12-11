import turtle
import math

bob = turtle.Turtle()


bob.color('black','#e6c619')

bob.pensize(3)
bob.penup()
bob.goto(-100,0)
bob.left(100)
bob.pendown()
bob.begin_fill()
bob.forward(70)
bob.right(130)
bob.forward(60)
bob.left(90)
bob.forward(60)
bob.right(120)
bob.forward(60)
bob.left(90)
bob.forward(60)
bob.right(130)
bob.forward(70)
bob.right(45)
bob.circle(-125,70)
bob.end_fill()
bob.penup()
bob.goto(-88,56)
bob.color('black','#e6c619')
bob.begin_fill()
bob.right(90)
bob.pendown()
bob.forward(35)
bob.right(90)
bob.forward(29)
bob.penup()
bob.right(85)
bob.forward(33)
bob.end_fill()
bob.setheading(0)
bob.forward(63)
bob.begin_fill()
bob.left(122)
bob.forward(33)
bob.pendown()
bob.right(90)
bob.forward(29)
bob.right(90)
bob.forward(32)
bob.end_fill()
turtle.penup()
turtle.goto(-30,0)
turtle.pendown()
turtle.color('black','#228b22')
turtle.begin_fill()
a = 10
b = 20
dx = turtle.xcor()
dy = turtle.ycor()
for deg in range(361):
    rad = math.radians(deg)
    x = a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    turtle.goto(x, y)
turtle.end_fill()
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.back(40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()













turtle.done()