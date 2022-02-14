"""EX04 - A beautiful flowery scene, courtesy of Turtle.

I used randomness to choose the flower colors and the flower locations (lines 42 - 55, 33, 44). I also
tried to make my flowers a more complex feature (lines 80-104, 107-117) and used Screen to color in 
the background of my scene (lines 20, 23).
"""

__author__ = "730480148"

import random
from random import randint
from turtle import Turtle, colormode, done, Screen, tracer, update
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)  # disable delay in tracing
    artist: Turtle = Turtle()
    sky = Screen()
    i: int = 0
    flower_color: str = ""
    sky.bgcolor(206, 236, 255)
    artist.speed(0)  # sets the turtle to draw at max speed
    # draws the scene of a sun, three clouds, a field, and flowers
    draw_sun(artist, -230, 200)
    draw_cloud(artist, 210, 170)
    draw_cloud(artist, -40, 180)
    draw_cloud(artist, -200, 150)
    draw_field(artist, -400, -100)
    # draws six flowers at random locations, with random colors
    while i < 6:
        x: float = random.uniform(-300, 300)  # generates a random x-coordinate for the flower
        y: float = random.uniform(-300, -130)  # generates a random y-coordinate for the flower
        flower_color = colorpicker()  # uses colorpicker function to generate color
        draw_flower(artist, flower_color, x, y)
        i += 1
    update()  # updates the rendering
    done()


def colorpicker() -> str:
    """Returns a color, in hexcode form, for the flowers."""
    picker: int = randint(0, 3)
    # depending on what random integer is returned, a different color
    # is returned
    if picker == 0:
        flower_color = "#FFDAF9"
    elif picker == 1:
        flower_color = "#F4FBA0"
    elif picker == 2:
        flower_color = "#8DA6F1"
    else:
        flower_color = "#D8BBEA"
    return flower_color
        

def draw_field(field: Turtle, x: float, y: float) -> None:
    """Draws a grassy field."""
    field.penup()
    field.goto(x, y)
    field.pendown()  # begins drawing
    field.color(104, 162, 81)
    field.begin_fill()
    field.setheading(0)
    field.right(90)
    i: int = 0
    # draws a rectangle
    while i < 2: 
        field.forward(300)
        field.left(90)
        field.forward(1400)
        field.left(90)
        i += 1
    field.left(90)
    field.end_fill()
    field.penup()


def draw_petal(petal: Turtle, color: str, x: float, y: float) -> None:
    """Draws one petal of a flower."""
    petal.penup()
    petal.goto(x, y)
    petal.pendown()  # begins drawing
    petal.pencolor("black")
    petal.fillcolor(color)
    petal.begin_fill()
    i: int = 0
    # draws one half of a petal
    while i < 50:
        petal.right(2)
        petal.forward(1)
        i += 1
    i = 0
    petal.left(99)
    # draws the other half
    while i < 50: 
        petal.right(2)
        petal.backward(1)
        i += 1
    petal.end_fill()
    petal.penup()
    petal.goto(x, y)
    petal.right(99)


def draw_flower(flower: Turtle, color: str, x: float, y: float) -> None:
    """Draws an elegant flower."""
    flower.penup()
    flower.goto(x, y)
    flower.pendown()  # begins drawing
    i: int = 0
    # creates seven petals
    while i < 7:
        draw_petal(flower, color, x, y)  # uses draw_petal function to draw petal
        flower.left(45)
        i += 1


def draw_cloud(cloud: Turtle, x: float, y: float) -> None:
    """Draws a fluffy, white cloud."""
    cloud.penup()
    cloud.goto(x, y)
    cloud.color("white", "white")
    cloud.pendown()  # begins drawing
    cloud.begin_fill()
    # uses semi-circles (180 degrees of a circle with radius 25) to draw a cloud
    cloud.circle(25, 180)
    cloud.right(90)
    cloud.circle(25, 180)
    cloud.right(180)
    cloud.circle(25, 180)
    cloud.right(90)
    cloud.circle(25, 180)
    cloud.right(90)
    cloud.circle(25, 180)
    cloud.right(180)
    cloud.circle(25, 180)
    cloud.end_fill()
    cloud.setheading(0)


def draw_sun(sun: Turtle, x: float, y: float) -> None:
    """Draws a beautiful sun."""
    sun.penup()
    sun.goto(x, y)
    sun.pendown()  # begins drawing
    sun.pencolor(255, 191, 0)
    sun.fillcolor(255, 243, 99)
    sun.begin_fill()
    sun.circle(50)  # draws circle with radius 50
    sun.end_fill()


if __name__ == "__main__":
    main()