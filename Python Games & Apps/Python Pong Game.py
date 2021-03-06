# May be you can't import turtle module in linux
# So do that command sudo apt-get install python3-tk
import turtle

wind = turtle.Screen()  # Intialize Screen
wind.title("Ping    Pong")  # Set the title of the windo
wind.bgcolor("black")  # Set the background color of the window
wind.setup(width=800, height=600)  # set the width and height of the windo
wind.tracer(0)  # Stop the window from updating automatically


# madrab1
madrab1 = turtle.Turtle()  # intialize turtle object (shape)
madrab1.speed(0)  # Set the speed of the animation
madrab1.shape("square")  # set the shape of the object
madrab1.color("blue")  # set the color of the shhape
# Set the width and length of the shape
madrab1.shapesize(stretch_wid=6, stretch_len=1)
madrab1.penup()  # Stops the object from drawing lines
madrab1.goto(-350, 0)  # se the position of the object

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=6, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .0250
ball.dy = .0250

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1:0  Pylyer 2:0", align="center",
            font=("Courier", 14, "normal"))

# Functions


def madrab1_up():
    y = madrab1.ycor()  # Get the y coordinate of madra1
    y += 20  # Set the y to increase be 20
    madrab1.sety(y)  # set the y of the madrab1 to the neew y coordinate


def madrab1_down():
    y = madrab1.ycor()
    y -= 20  # Set the y to decrease be 20
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


# Main game loop
while True:
    wind.update()

    # move the ball
    # ball stars at zero and evrytime loops run--->+.025 xaxis
    ball.setx(ball.xcor() + ball.dx)
    # ball stars at zero and evrytime loops run--->+.025 yaxis
    ball.sety(ball.ycor() + ball.dy)

    # border chek , top border +300px, bottom border -300 bx , ball is 20px
    if ball.ycor() > 290:  # if ball is at top borrder
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction, making +.025 --> -.025

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball is at right border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse the x dirction
        score1 += 1
        score.clear()
        score.write("Player 1:{}  Pylyer 2:{}".format(score1, score2), align="center",
                    font=("Courier", 14, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1:{}  Pylyer 2:{}".format(score1, score2), align="center",
                    font=("Courier", 14, "normal"))

    # Tasadom madrab and ball

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > - 350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
