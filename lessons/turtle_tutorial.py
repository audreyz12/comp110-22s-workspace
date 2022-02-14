from turtle import Turtle, colormode, done
# enable RGB
colormode(255)
leo: Turtle = Turtle()

# RGB values
leo.color(99, 204, 250)
leo.penup()
leo.goto(-100, 0)
leo.pendown()

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
done()
# to set only pen color
leo.pencolor("pink")
# to set only fill color
leo.fillcolor(32, 67, 93)
# to set fill and pen color
leo.color("green," "yellow")

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()

index: int = 0
side_length: float = 300
bob.color("black")
bob.pendown()
while (index < 20):
    bob.forward(side_length)
    bob.left(122)
    side_length = side_length * 0.97
    i += 1
done()