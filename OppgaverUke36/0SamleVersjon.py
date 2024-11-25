import turtle

# Opprette vindu
flagg_skjerm = turtle.Turtle

# Opprette spørredialog
velg_flagg = turtle.Screen()

# Viser valgene og lar bruker velge flagg som gir variabel som tegner riktig flagg
flagg_valg = velg_flagg.textinput("Velkommen til dette programmet som tegner nordiske flagg!",
                                  "Velg mellom Danmark, Island, Finland, Sverige, Åland, Færøyene, "
                                  "Grønland, Norge og Same- flagget"
                                  )
if flagg_valg == "Island":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#0048e0")
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-370, -40)
    turtle.pendown()
    turtle.pencolor("#ffffff")
    turtle.fillcolor("#ffffff")

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

    turtle.pencolor("#d72828")
    turtle.fillcolor("#d72828")
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
elif flagg_valg == "Danmark":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#C8102E")
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-370, -40)
    turtle.pendown()
    turtle.pencolor("#ffffff")
    turtle.fillcolor("#ffffff")
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

    turtle.exitonclick()
elif flagg_valg == "Finland":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#ffffff")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-370, -40)
    turtle.pendown()
    turtle.pencolor("#002F6C")
    turtle.fillcolor("#002F6C")
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

    turtle.exitonclick()
elif flagg_valg == "Norge":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#BA0C2F")
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-370, -40)
    turtle.pendown()
    turtle.pencolor("#ffffff")
    turtle.fillcolor("#ffffff")

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

    turtle.pencolor("#00205B")
    turtle.fillcolor("#00205B")
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
elif flagg_valg == "Færøyene":
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
elif flagg_valg == "Grønland":
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
elif flagg_valg == "Same- flagget":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#0038A8")
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-740, -280)
    turtle.pendown()
    turtle.pencolor("#D81E05")
    turtle.fillcolor("#D81E05")

    turtle.begin_fill()

    turtle.forward(640)
    turtle.left(90)
    turtle.forward(740)
    turtle.left(90)
    turtle.forward(640)
    turtle.left(90)
    turtle.forward(740)

    turtle.end_fill()

    turtle.goto(-100, -280)
    turtle.pencolor("#007A3D")
    turtle.fillcolor("#007A3D")

    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(740)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(740)

    turtle.end_fill()

    turtle.goto(-50, -280)
    turtle.pencolor("#FCD116")
    turtle.fillcolor("#FCD116")

    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(740)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(740)

    turtle.end_fill()
    turtle.penup()

    turtle.fillcolor("#D81E05")
    turtle.goto(-250, 0)
    turtle.pendown()
    turtle.pensize(30)
    turtle.pencolor("#D81E05")
    turtle.circle(200, 270)
    turtle.pencolor("#0038A8")
    turtle.circle(200, 180)

    turtle.penup()
    turtle.goto(-50, 185)
    turtle.pensize(1)
    turtle.pencolor("#D81E05")
    turtle.pendown()
    turtle.fillcolor("#D81E05")
    turtle.begin_fill()
    turtle.circle(15, 180)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-50, -185)
    turtle.pensize(1)
    turtle.pencolor("#D81E05")
    turtle.pendown()
    turtle.fillcolor("#D81E05")
    turtle.begin_fill()
    turtle.circle(15, -180)
    turtle.end_fill()

    turtle.exitonclick()
elif flagg_valg == "Åland":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#ffffff")
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-370, -40)
    turtle.pendown()
    turtle.pencolor("#0065BD")
    turtle.fillcolor("#0065BD")

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

    turtle.pencolor("#ED2939")
    turtle.fillcolor("#ED2939")
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
elif flagg_valg == "Sverige":
    tf = turtle.Screen()
    tf.setup(width=740, height=560)
    tf.bgcolor("#006AA7")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-370, -40)
    turtle.pendown()
    turtle.pencolor("#FFCD00")
    turtle.fillcolor("#FFCD00")
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

    turtle.exitonclick()
else:
    turtle.hideturtle()
    turtle.write("Error. Du må velge et av alternativene.\nStart programmet på nytt",
                 align="center", font=("Arial", 30, "normal"))
    turtle.exitonclick()
