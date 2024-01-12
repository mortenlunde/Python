import turtle

tf = turtle.Screen()
tf.setup(width=740, height=560)
tf.bgcolor("#0064AD")
turtle.hideturtle()
turtle.speed(10)
turtle.penup()
turtle.goto(-370, -40)
turtle.pendown()
turtle.pencolor("#FFD300")
turtle.fillcolor("#FFD300")

turtle.begin_fill()

turtle.forward(230)
turtle.right(90)
turtle.forward(230)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(230)
turtle.right(90)
turtle.forward(430)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(430)
turtle.right(90)
turtle.forward(230)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(230)
turtle.right(90)
turtle.forward(230)
turtle.left(90)
turtle.forward(100)

turtle.end_fill()

turtle.pencolor("#DA0E15")
turtle.fillcolor("#DA0E15")
turtle.begin_fill()
turtle.left(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()

turtle.exitonclick()
