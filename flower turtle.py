import turtle

bob = turtle.Turtle()

bob.color("red", "cyan")

bob.begin_fill()

for i in range(60):

    bob.speed(0)
    bob.forward(250)
    bob.left(174)

bob.end_fill()

bob.penup()

bob.left(1.6)
bob.forward(125)
bob.right(90)

bob.pendown()

bob.forward(300)
bob.left(180)
bob.forward(120)
bob.right(90)
bob.forward(80)
bob.left(40)
bob.forward(50)
bob.right(65)
bob.forward(90)
bob.right(50)
bob.right(80)
bob.forward(90)
bob.right(75)
bob.forward(57)
bob.left(50)
bob.forward(50)
bob.left(180)
bob.forward(110)
bob.right(6)
bob.forward(57)

turtle.done()