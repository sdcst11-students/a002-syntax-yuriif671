import turtle

s = turtle.getscreen()
t = turtle.Turtle()

#make a red circle
t.penup()
t.goto(-100, 50)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.circle(45)
t.end_fill()

#make a blue triangle
t.penup()
t.goto(100, 50)
t.pendown()

t.fillcolor("blue")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(142)
t.right(225)

t.end_fill()

#draw blue sky, green grass and the sun
#blue sky
t.penup()
t.goto(-200, -100)
t.pendown()

t.fillcolor("light blue")
t.begin_fill()

for i in range(2):
    t.forward(500)
    t.rt(90)
    t.forward(250)
    t.rt(90)

t.end_fill()

#green grass
t.penup()
t.rt(90)
t.fd(225)

t.fillcolor("green")
t.begin_fill()
t.pendown()

t.lt(90)

for i in range(2):
    t.fd(500)
    t.rt(90)
    t.fd(25)
    t.rt(90)

t.end_fill()

#make a sun
t.penup()
t.forward(250)
t.lt(65)

t.forward(150)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(45)
t.end_fill()

#do a spin for people to look at it
for i in range(20):
    t.lt(45)