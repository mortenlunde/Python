from turtle import *
from random import randint

# Screen
SIZE = 500

SCREEN = Screen()
SCREEN.setup(SIZE + 50, SIZE + 50)
SCREEN.bgcolor("black")

#Food
food = Turtle()
food.up()
food.shape("circle")
food.color("yellow")
food.hideturtle()

#Snake
snake = Turtle()
snake.up()
snake.shape("circle")
snake.color("green")
snake.hideturtle()

# Random food- position
def getRandomPosition():
    position = (randint(-SIZE//2, SIZE//2), randint(-SIZE//2, SIZE//2))
    return position

food_coordinates = getRandomPosition()

#Coordinates for the snake
snake_coordinates = [(0, 0)]

#List of stamps
stamps = []

#Directions
dir_x = 0
dir_y = 0

#Acutalise the display
def actualise_display():
    tracer = SCREEN.tracer()
    SCREEN.tracer(0)
    
    food.clearstamps(1)
    snake.clearstamps(len(snake_coordinates))
    
    food.goto(food_coordinates[0], food_coordinates[1])
    food.stamp()
    
    for x, y in snake_coordinates:
        snake.goto(x, y)
        snake.stamp()
        
#Is there a collision?
stop = False

def actualise_position():
    global snake_coordinates, food_coordinates, stop
    avance()
    if isSelfCollision():
        stop = True
    elif isBorderCollision():
        stop = True
    elif isFoodCollision():
        append()
        food_coordinates = getRandomPosition()

#GameLoop
def loop():
    if stop:
        gameOver()
        return
    actualise_position()
    actualise_display()
    SCREEN.ontimer(loop, 100)

#Return true if self collision
def isSelfCollision():
    global snake_coordinates
    check = len(set(snake_coordinates)) < len(snake_coordinates)
    return check

#Return true if bordercollision
def isBorderCollision():
    x, y = snake_coordinates[0]
    return not (-SIZE//2 - 50 < x < SIZE//2 + 50) or not (-SIZE//2 - 50 < y < SIZE//2 + 50)

#Returns true if eat food
def isFoodCollision():
    sx, sy = snake_coordinates[0]
    fx, fy = food_coordinates
    distance = ((sx - fx)**2 + (sy - fy)**2)**.5
    return distance < 20

#Moves the snake
def avance():
    global snake_coordinates
    x, y = snake_coordinates[0]
    x = x + dir_x*20
    y = y + dir_y*20
    snake_coordinates.insert(0, (x, y))
    snake_coordinates.pop()
    
#Makes the snake bigger
def append():
    global snake_coordinates
    grow = snake_coordinates[-1][:]
    snake_coordinates.append(grow)
    
#Moving around
def setDirection(x, y):
    global dir_x, dir_y
    dir_x = x
    dir_y = y

def right():
    setDirection(1, 0)
    
def left():
    setDirection(-1, 0)
    
def up():
    setDirection(0, 1)
    
def down():
    setDirection(0, -1)

#When game over
def gameOver():
    d = Turtle()
    d.up()
    d.hideturtle()
    d.color("blue")
    d.write("GAME OVER \nScore : %04d" % (len(snake_coordinates)), align="center", font=("arial", 40, "bold"))
    SCREEN.onclick(lambda*a:[SCREEN.bye(), exit()])

#Moving around when click
SCREEN.onkeypress(up, "Up")
SCREEN.onkeypress(down, "Down")
SCREEN.onkeypress(left, "Left")
SCREEN.onkeypress(right, "Right")
SCREEN.listen()

loop()

# Hold vinduet åpent
SCREEN.mainloop()
