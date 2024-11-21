import turtle

# Jeg lager en turtle
min_turtle = turtle.Turtle()
min_turtle.shape('turtle')

# Endre hastighet
min_turtle.speed(10)

# Vi tegner på skjerm
min_turtle.fillcolor('blue')
min_turtle.begin_fill()
for i in range(4):
    min_turtle.forward(100)
    min_turtle.left(90)
min_turtle.end_fill()

min_turtle.right(135)

# før vi går, løft opp penn
min_turtle.penup()
min_turtle.forward(200)
min_turtle.left(135)
min_turtle.pendown()

min_turtle.pencolor('red')
min_turtle.fillcolor('red')
min_turtle.begin_fill()
min_turtle.circle(100)
min_turtle.end_fill()

min_turtle.left(90)
min_turtle.penup()
min_turtle.forward(300)
min_turtle.pendown()
min_turtle.pencolor('green')
min_turtle.fillcolor('green')
min_turtle.begin_fill()
min_turtle.right(90)
for i in range(2):
    min_turtle.forward(150)
    min_turtle.left(120)
min_turtle.hideturtle()
min_turtle.end_fill()

# Avslutt med stil
turtle.exitonclick()
