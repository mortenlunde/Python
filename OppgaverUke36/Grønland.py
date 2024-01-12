import turtle

tf = turtle.Screen()
tf.setup(width=740, height=560)
tf.bgcolor("#ffffff")
turtle.hideturtle()
turtle.speed(10)
turtle.penup()
turtle.goto(-370, 0)
turtle.pendown()
turtle.pencolor("#D00C33")
turtle.fillcolor("#D00C33")

turtle.begin_fill()

turtle.right(90)

for n in range(2):
    turtle.forward(270)
    turtle.left(90)
    turtle.forward(740)
    turtle.left(90)

turtle.end_fill()

turtle.fillcolor("#ffffff")
turtle.begin_fill()
turtle.goto(-250, 0)
turtle.circle(150, 180)
turtle.end_fill()
turtle.fillcolor("#D00C33")
turtle.begin_fill()
turtle.circle(150, 180)
turtle.end_fill()

turtle.exitonclick()