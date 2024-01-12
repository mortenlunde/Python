import turtle
import random
from typing import List

COLORS = ('yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray')

DIRECTION_RIGHT = 0
DIRECTION_UP = 90
DIRECTION_LEFT = 180
DIRECTION_DOWN = 270

START_X = -300
END_X = 300
MIN_Y = -100
#


def create_turtle(color: str) -> turtle.Turtle:
    p = turtle.Turtle()
    p.color(color)
    p.shape("turtle")
    return p


def create_turtles(count: int) -> List[turtle.Turtle]:
    turtles = []
    for colr in random.sample(COLORS, count):
        turtles.append(create_turtle(colr))
    return turtles


def create_track(trtle: turtle.Turtle,
                 startpos: tuple[int, int],
                 length: int,
                 direction: int,
                 text: str):
    trtle.hideturtle()
    trtle.penup()
    trtle.goto(startpos)
    trtle.setheading(direction)
    trtle.pendown()
    trtle.pendown()
    trtle.forward(length)
    trtle.write(text)


def write_result(draw_turtle: turtle.Turtle,
                 startpos: tuple[int, int],
                 results: List[turtle.Turtle]):
    draw_turtle.penup()
    draw_turtle.goto(startpos)
    font = ("Arial", 16, "normal")
    draw_turtle.write("Resultatliste", font=font)

    x, y = startpos
    offset = 20
    y -= offset
    for idx, p in enumerate(results):
        draw_turtle.goto(x, y)
        draw_turtle.pencolor(p.color()[0])
        draw_turtle.write(f"Spiller {idx + 1}: {p.color()[0]}", font=font)
        y -= 20


def sort_by_x_pos(t: turtle.Turtle) -> float:
    return t.xcor()
