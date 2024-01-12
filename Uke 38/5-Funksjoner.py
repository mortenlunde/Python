import turtle

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.goto(-500, 0)
my_turtle.pendown()

COLORS = ["blue", "red", "green", "yellow", "black", "orange", "magenta"]


def lagfirkant(lengde, farge):
    my_turtle.fillcolor(farge)
    my_turtle.begin_fill()

    for _ in range(4):
        my_turtle.forward(lengde)
        my_turtle.left(90)

    my_turtle.end_fill()


def flyttmarkor(lengde):
    my_turtle.penup()
    my_turtle.forward(lengde)
    my_turtle.pendown()


for i in range(100, 0, -10):
    lagfirkant(i, "#EF2B2D")
    flyttmarkor(i)
for i in range(0, 101, 10):
    lagfirkant(i, "#EF2B2D")
    flyttmarkor(i)
my_turtle.hideturtle()

turtle.exitonclick()
