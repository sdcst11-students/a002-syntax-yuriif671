#navigate the maze

import turtle

s = turtle.getscreen()
s.bgpic('maze.gif')
t = turtle.Turtle()

#go to start
t.penup()
t.goto(-200, 100)

t.pendown()
t.rt(90)
t.fd(100)

t.lt(90)
t.fd(50)

t.rt(90)
t.fd(50)

t.rt(90)
t.fd(50)

t.lt(90)
t.fd(50)

t.lt(90)
t.fd(145)

t.lt(90)
t.fd(50)

t.rt(45)
t.fd(50)

t.lt(45)
t.fd(50)

t.lt(90)
t.fd(60)

t.rt(90)
t.fd(60)

t.rt(90)
t.fd(80)

t.rt(45)
t.fd(100)

t.lt(135)
t.fd(70)

t.rt(90)
t.fd(150)

t.rt(90)
t.fd(25)

t.rt(45)
t.fd(100)

t.lt(45)
t.fd(50)

t.rt(90)
t.fd(25)

t.lt(90)
t.fd(50)

t.lt(90)
t.fd(80)

t.rt(90)
t.fd(50)

#do a spin
for i in range(100):
    t.lt(45)