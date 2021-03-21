# May be you can't import turtle module in linux
# So do that command sudo apt-get install python3-tk
import turtle

wind = turtle.Screen()  # intialize screen
wind.title("Ping    Pong")  # set the title of the windo
wind.bgcolor("black")  # set the background color of the window
wind.setup(width=800, height=600)  # set the width and height of the windo
wind.tracer(0)  # stop the window from updating automatically


# madrab1
madrab1 = turtle.Turtle()  # intialize turtle object (shape)
madrab1.speed(0)  # set the speed of the animation
madrab1.shape("square")  # set the shape of the object
madrab1.color("blue")  # set the color of the shhape
# set the width and length of the shape
madrab1.shapesize(stretch_wid=6, stretch_len=1)
madrab1.penup()  # stops the object from drawing lines
madrab1.goto(-350, 0)  # se the position of the object

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=6, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .025
ball.dy = -.025


# functions


def madrab1_up():
    y = madrab1.ycor()  # get the y coordinate of madra1
    y += 20  # set the y to increase be 20
    madrab1.sety(y)  # set the y of the madrab1 to the neew y coordinate


def madrab1_down():
    y = madrab1.ycor()
    y -= 20  # set the y to decrease be 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard bindins
wind.listen()  # tell the windo to expect keboard inpot
# when pressing w thw function madrab1_up is invoked
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")

wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")


# main game loop
while True:
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border chek
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
